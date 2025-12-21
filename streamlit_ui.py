"""
Meta-Agent Factory - Streamlit UI
Provides interactive web interface for agent generation
"""

import streamlit as st
import json
import os
from dotenv import load_dotenv
from typing import Any

# Load environment
load_dotenv(override=True)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Meta-Agent Factory",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        font-weight: 600;
    }
    .step-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
    }
    .strategy-box {
        border: 2px solid #ddd;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .blueprint-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    .code-box {
        background: #1e1e1e;
        color: #d4d4d4;
        padding: 1.5rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.user_request = ""
    st.session_state.strategies = None
    st.session_state.selected_strategy = None
    st.session_state.blueprint = None
    st.session_state.generated_code = None
    st.session_state.history = []

# ============================================================================
# MAIN UI
# ============================================================================

# Header
col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.markdown("# 🤖")
with col2:
    st.markdown("# Meta-Agent Factory")
    st.markdown("*Automatically generate working AI agents from descriptions*")

st.divider()

# ============================================================================
# STEP 1: USER INPUT
# ============================================================================

st.markdown("### Step 1️⃣: Describe Your Agent")
st.markdown("Tell us what agent you need, and we'll generate it for you.")

user_request = st.text_area(
    "What kind of agent do you need?",
    value=st.session_state.user_request,
    height=150,
    placeholder="Example: I need a customer support agent that can access our knowledge base, send emails, and create support tickets...",
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns(3)

with col1:
    generate_btn = st.button(
        "✨ Generate Strategies",
        key="generate_btn",
        use_container_width=True,
        type="primary"
    )

with col2:
    st.button("📚 View Examples", use_container_width=True)

with col3:
    st.button("💾 Load from History", use_container_width=True)

if generate_btn and user_request:
    st.session_state.user_request = user_request
    st.session_state.step = 2
    
    # Simulate consultant agent response
    st.session_state.strategies = {
        "strategy_a": {
            "name": "Rule-Based Approach",
            "description": "Uses predefined rules and patterns to handle support requests",
            "pros": [
                "Fast response time",
                "Predictable behavior",
                "Easy to debug",
                "Good for known patterns"
            ],
            "cons": [
                "Limited flexibility",
                "Needs manual rule updates",
                "Can't handle novel cases"
            ],
            "estimated_time": "2-3 hours",
            "estimated_cost": "$150"
        },
        "strategy_b": {
            "name": "ML-Based Approach",
            "description": "Uses machine learning models to understand and respond to support requests",
            "pros": [
                "Learns from interactions",
                "Handles novel cases",
                "Improves over time",
                "Better language understanding"
            ],
            "cons": [
                "Requires training data",
                "Slower initial setup",
                "Harder to debug",
                "May need fine-tuning"
            ],
            "estimated_time": "1-2 days",
            "estimated_cost": "$500"
        }
    }
    
    st.success("✨ Strategies generated!")
    st.rerun()

# ============================================================================
# STEP 2: STRATEGY SELECTION
# ============================================================================

if st.session_state.step >= 2 and st.session_state.strategies:
    st.divider()
    st.markdown("### Step 2️⃣: Choose Your Strategy")
    st.markdown("Select the architecture that best fits your needs.")
    
    tab_a, tab_b = st.tabs(["Strategy A: Rule-Based", "Strategy B: ML-Based"])
    
    with tab_a:
        st.markdown("#### Rule-Based Approach")
        strategy_a = st.session_state.strategies["strategy_a"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Pros:**")
            for pro in strategy_a["pros"]:
                st.markdown(f"✅ {pro}")
        
        with col2:
            st.markdown("**Cons:**")
            for con in strategy_a["cons"]:
                st.markdown(f"⚠️ {con}")
        
        st.markdown(f"**Estimated Time:** {strategy_a['estimated_time']}")
        st.markdown(f"**Estimated Cost:** {strategy_a['estimated_cost']}")
        
        if st.button("Select Strategy A", key="select_a", use_container_width=True, type="primary"):
            st.session_state.selected_strategy = "strategy_a"
            st.session_state.step = 3
            st.rerun()
    
    with tab_b:
        st.markdown("#### ML-Based Approach")
        strategy_b = st.session_state.strategies["strategy_b"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Pros:**")
            for pro in strategy_b["pros"]:
                st.markdown(f"✅ {pro}")
        
        with col2:
            st.markdown("**Cons:**")
            for con in strategy_b["cons"]:
                st.markdown(f"⚠️ {con}")
        
        st.markdown(f"**Estimated Time:** {strategy_b['estimated_time']}")
        st.markdown(f"**Estimated Cost:** {strategy_b['estimated_cost']}")
        
        if st.button("Select Strategy B", key="select_b", use_container_width=True, type="primary"):
            st.session_state.selected_strategy = "strategy_b"
            st.session_state.step = 3
            st.rerun()

# ============================================================================
# STEP 3: BLUEPRINT APPROVAL
# ============================================================================

if st.session_state.step >= 3 and st.session_state.selected_strategy:
    st.divider()
    st.markdown("### Step 3️⃣: Review Blueprint")
    st.markdown(f"Selected strategy: **{st.session_state.strategies[st.session_state.selected_strategy]['name']}**")
    
    if st.session_state.blueprint is None:
        # Generate blueprint (simulated)
        st.session_state.blueprint = {
            "agent_name": "CustomerSupportAgent",
            "description": st.session_state.user_request,
            "strategy": st.session_state.selected_strategy,
            "components": [
                {
                    "name": "RequestAnalyzer",
                    "type": "NLP",
                    "purpose": "Analyze incoming support requests"
                },
                {
                    "name": "KnowledgeBaseLookup",
                    "type": "Tool",
                    "purpose": "Search knowledge base for answers"
                },
                {
                    "name": "TicketCreator",
                    "type": "Tool",
                    "purpose": "Create support tickets in system"
                },
                {
                    "name": "EmailNotifier",
                    "type": "Tool",
                    "purpose": "Send email responses"
                }
            ],
            "tools_required": [
                "knowledge_base_api",
                "ticket_system_api",
                "email_service"
            ],
            "estimated_setup_time": "2-3 hours",
            "estimated_cost": "$150"
        }
    
    # Display blueprint
    col1, col2 = st.columns([0.6, 0.4])
    
    with col1:
        st.markdown("**Blueprint Overview:**")
        st.json(st.session_state.blueprint)
    
    with col2:
        st.markdown("**System Components:**")
        for comp in st.session_state.blueprint["components"]:
            with st.container(border=True):
                st.markdown(f"**{comp['name']}**")
                st.markdown(f"*{comp['type']}*")
                st.markdown(f"{comp['purpose']}")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✅ Approve Blueprint", key="approve", use_container_width=True, type="primary"):
            st.session_state.step = 4
            st.success("Blueprint approved! Generating code...")
            st.rerun()
    
    with col2:
        if st.button("✏️ Request Changes", key="request_changes", use_container_width=True):
            with st.form("changes_form"):
                changes = st.text_area("What should we change?")
                if st.form_submit_button("Submit Changes"):
                    st.info("Revising blueprint based on your feedback...")
                    st.rerun()
    
    with col3:
        if st.button("↩️ Back", use_container_width=True):
            st.session_state.step = 2
            st.rerun()

# ============================================================================
# STEP 4: CODE GENERATION & DOWNLOAD
# ============================================================================

if st.session_state.step >= 4 and st.session_state.blueprint:
    st.divider()
    st.markdown("### Step 4️⃣: Your Generated Agent Code")
    st.markdown("Here's your complete, working agent code:")
    
    if st.session_state.generated_code is None:
        # Generate code (simulated)
        st.session_state.generated_code = '''"""
Generated AI Agent - CustomerSupportAgent
Created by Meta-Agent Factory
"""

from typing import Any, Optional
import asyncio
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.tools import Tool
import json

# ============================================================================
# CONFIGURATION
# ============================================================================

class AgentConfig:
    """Agent configuration"""
    MODEL = "gpt-4o"
    TEMPERATURE = 0.7
    MAX_RETRIES = 3
    TIMEOUT = 30

# ============================================================================
# TOOL DEFINITIONS
# ============================================================================

def search_knowledge_base(query: str) -> str:
    """Search company knowledge base for answers"""
    # Mock implementation - replace with real API
    return f"Found answer for: {query}"

def create_support_ticket(issue: str, priority: str) -> str:
    """Create support ticket in system"""
    # Mock implementation - replace with real API
    return f"Ticket created: {issue[:30]}... (Priority: {priority})"

def send_email(recipient: str, subject: str, body: str) -> str:
    """Send email to customer"""
    # Mock implementation - replace with real API
    return f"Email sent to {recipient}"

# ============================================================================
# AGENT SETUP
# ============================================================================

tools = [
    Tool(
        name="SearchKnowledgeBase",
        func=search_knowledge_base,
        description="Search company knowledge base for answers to customer questions"
    ),
    Tool(
        name="CreateTicket",
        func=create_support_ticket,
        description="Create a support ticket when issue needs escalation"
    ),
    Tool(
        name="SendEmail",
        func=send_email,
        description="Send email response to customer"
    )
]

class CustomerSupportAgent:
    """Customer Support Agent"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=AgentConfig.MODEL,
            temperature=AgentConfig.TEMPERATURE
        )
        self.agent = create_openai_tools_agent(self.llm, tools, prompt=None)
        self.executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent,
            tools=tools,
            verbose=True
        )
    
    async def handle_request(self, request: str) -> str:
        """Process customer support request"""
        try:
            result = await self.executor.ainvoke({"input": request})
            return result["output"]
        except Exception as e:
            return f"Error processing request: {str(e)}"
    
    async def run(self):
        """Run agent in interactive mode"""
        print("🤖 Customer Support Agent Started")
        print("Type 'exit' to quit")
        print("-" * 50)
        
        while True:
            user_input = input("Customer: ").strip()
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            response = await self.handle_request(user_input)
            print(f"Agent: {response}")
            print("-" * 50)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    agent = CustomerSupportAgent()
    asyncio.run(agent.run())
'''
    
    # Code display
    st.code(st.session_state.generated_code, language="python")
    
    st.markdown("---")
    
    # Action buttons
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.download_button(
            label="📥 Download Code",
            data=st.session_state.generated_code,
            file_name="agent.py",
            mime="text/plain",
            use_container_width=True
        )
    
    with col2:
        st.button(
            "📋 Copy to Clipboard",
            use_container_width=True,
            help="Copy code to clipboard"
        )
    
    with col3:
        st.button(
            "▶️ Run Test",
            use_container_width=True,
            help="Test the generated agent"
        )
    
    with col4:
        st.button(
            "🔄 Regenerate",
            use_container_width=True,
            help="Regenerate code with different parameters"
        )
    
    st.divider()
    
    # Next steps
    st.markdown("### Next Steps")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.markdown("**1️⃣ Setup**")
            st.markdown("""
            - Install dependencies
            - Configure API keys
            - Set up data sources
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("**2️⃣ Customize**")
            st.markdown("""
            - Adjust parameters
            - Add custom tools
            - Fine-tune responses
            """)
    
    with col3:
        with st.container(border=True):
            st.markdown("**3️⃣ Deploy**")
            st.markdown("""
            - Test thoroughly
            - Deploy to production
            - Monitor performance
            """)

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("### 📊 Agent Stats")
    
    st.metric("Current Step", f"{st.session_state.step}/4")
    
    if st.session_state.user_request:
        st.metric("Request Length", len(st.session_state.user_request))
    
    if st.session_state.generated_code:
        st.metric("Code Lines", len(st.session_state.generated_code.split('\n')))
    
    st.divider()
    
    st.markdown("### 🔧 Settings")
    
    model = st.selectbox("LLM Model", ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    st.divider()
    
    st.markdown("### 📚 Resources")
    
    st.markdown("""
    - [LangChain Docs](https://python.langchain.com/)
    - [OpenAI API](https://platform.openai.com/)
    - [MCP Protocol](https://modelcontextprotocol.io/)
    """)
    
    st.divider()
    
    st.markdown("### ℹ️ About")
    st.markdown("""
    **Meta-Agent Factory**
    
    Automatically generate working AI agents from descriptions using:
    - LangChain + LangGraph
    - OpenAI GPT-4o
    - MCP Tool Integration
    
    Version: 1.0.0
    """)
