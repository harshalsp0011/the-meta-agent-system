# 🔗 LangChain Version - Detailed Documentation

## 📋 Overview

This document provides in-depth technical documentation for the **LangChain + LangGraph** implementation of the Meta-Agent Factory System.

**File Location:** `src/root_LangChain_version.ipynb`

---

## 🏗️ Architecture Deep Dive

### LangGraph StateGraph Fundamentals

#### What is LangGraph?

LangGraph is a library for building **stateful, multi-agent applications** with LLMs. It's built on top of LangChain and provides:

- **StateGraph**: Directed graph for agent workflows
- **Nodes**: Individual agent functions
- **Edges**: Connections defining flow
- **State Management**: Shared memory across agents
- **Conditional Routing**: Dynamic flow control

#### Core Concepts

```python
from langgraph.graph import StateGraph, END

# 1. Define State (shared memory)
class MyState(TypedDict):
    field1: str
    field2: int

# 2. Create graph
graph = StateGraph(MyState)

# 3. Add nodes (agents)
graph.add_node("agent1", agent1_function)

# 4. Add edges (flow)
graph.add_edge("agent1", "agent2")

# 5. Compile
app = graph.compile()

# 6. Execute
result = app.invoke({"field1": "value"})
```

---

## 🧠 State Management

### FactoryState Definition

```python
class FactoryState(TypedDict):
    """
    Shared state that flows through the agent pipeline.
    
    This TypedDict ensures type safety and provides IDE support.
    All agents read from and write to this state.
    """
    
    # Input
    user_initial_request: str
    """Original problem description from user"""
    
    # Consultation Phase
    consultant_options: str
    """2-3 architectural approaches proposed by Consultant"""
    
    user_strategy_choice: str
    """User's selected strategy (e.g., 'Option 1')"""
    
    # Architecture Phase
    current_blueprint: str
    """JSON blueprint from Architect"""
    
    user_feedback: str
    """User's revision requests for blueprint"""
    
    # Build Phase
    final_code: str
    """Generated Python code from Builder"""
    
    # Status Tracking
    status: str
    """
    Current workflow state:
    - 'planning': Initial consultation
    - 'waiting_for_user_strategy': Awaiting strategy selection
    - 'reviewing': Architecture design
    - 'waiting_for_approval': Awaiting blueprint approval
    - 'revision_requested': User wants changes
    - 'approved': Blueprint approved
    - 'coding': Code generation in progress
    - 'finished': Complete
    """
```

### State Flow Diagram

```
Initial State
    │
    ├─► user_initial_request: "I want a shopping agent"
    │
    ▼
Consultant Updates
    │
    ├─► consultant_options: "Option 1: ...\nOption 2: ..."
    ├─► status: "waiting_for_user_strategy"
    │
    ▼
User Input
    │
    ├─► user_strategy_choice: "Option 1"
    │
    ▼
Architect Updates
    │
    ├─► current_blueprint: "{...JSON...}"
    ├─► status: "waiting_for_approval"
    │
    ▼
[Revision Loop]
    │
    ├─► IF approved:
    │   └─► status: "approved"
    │       └─► GO TO Builder
    │
    └─► IF revision_requested:
        ├─► user_feedback: "Add verification step"
        ├─► status: "revision_requested"
        └─► LOOP BACK TO Architect
    
    ▼
Builder Updates
    │
    ├─► final_code: "# Generated code..."
    ├─► status: "finished"
    │
    ▼
Complete
```

---

## 🤖 Agent Nodes

### 1. Consultant Node 👔

**Purpose:** Analyze request and propose architectural strategies

**Implementation:**
```python
def consultant_node(state: FactoryState) -> dict:
    """
    Consultant Agent: Strategic analysis and option proposal.
    
    Input from state:
        - user_initial_request: User's vague requirement
    
    Output to state:
        - consultant_options: 2-3 architectural approaches
        - status: "waiting_for_user_strategy"
    
    Prompt Strategy:
        - Ask for Simple, Moderate, and Complex options
        - Explain trade-offs for each
        - Be concise but specific
    """
    print("\n--- 👔 CONSULTANT IS THINKING ---")
    
    # Construct strategic analysis prompt
    prompt = f"""
    You are an AI Solutions Consultant. The user wants: "{state['user_initial_request']}".
    
    Your task: Propose 2 distinct architectural options for an AI Agent system to solve this.
    1. A Simple/Direct approach (faster, fewer components, good for MVP)
    2. A Complex/Comprehensive approach (robust, scalable, production-ready)
    
    Be concise but specific about the agent roles and workflow in each option.
    """
    
    # Invoke LLM
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Return state updates
    return {
        "consultant_options": response.content,
        "status": "waiting_for_user_strategy"
    }
```

**Key Design Decisions:**
- ✅ Returns dictionary (not full state) - merged automatically
- ✅ Updates status to trigger workflow pause
- ✅ Simple, focused responsibility
- ✅ No side effects (pure function)

---

### 2. Architect Node 📐

**Purpose:** Design JSON blueprint with iterative refinement

**Implementation:**
```python
def architect_node(state: FactoryState) -> dict:
    """
    Architect Agent: Blueprint design with feedback incorporation.
    
    Input from state:
        - user_initial_request: Original requirement
        - user_strategy_choice: Selected strategy
        - user_feedback: (Optional) Revision requests
    
    Output to state:
        - current_blueprint: JSON system design
        - status: "waiting_for_approval"
    
    Special Features:
        - Revision Loop: Checks for user_feedback
        - Context Awareness: Incorporates previous feedback
        - JSON Validation: Ensures valid structure
    """
    print("\n--- 📐 ARCHITECT IS DESIGNING ---")
    
    # Check for revision feedback
    feedback_context = ""
    if state.get("user_feedback"):
        feedback_context = f"""
        USER FEEDBACK ON PREVIOUS DRAFT: {state['user_feedback']}
        Fix the design accordingly. Address all concerns mentioned above.
        """
    
    # Construct design prompt
    prompt = f"""
    You are a Systems Architect specializing in AI agent systems.
    
    User Goal: {state['user_initial_request']}
    Selected Strategy: {state['user_strategy_choice']}
    {feedback_context}

    Design a JSON blueprint for this agent system with the following structure:
    {{
      "system_name": "descriptive_name",
      "agents": [
        {{
          "name": "AgentName",
          "role": "What this agent does",
          "tools": ["tool1", "tool2"]
        }}
      ],
      "flow": "Sequential" or "Parallel" or "Conditional"
    }}
    
    Output ONLY the JSON. No explanations, no markdown formatting.
    """
    
    # Invoke LLM
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Clean markdown code fencing
    blueprint = response.content.replace("```json", "").replace("```", "").strip()
    
    return {
        "current_blueprint": blueprint,
        "status": "waiting_for_approval"
    }
```

**Blueprint Schema:**
```typescript
interface Blueprint {
  system_name: string;
  description?: string;
  agents: Agent[];
  flow: "Sequential" | "Parallel" | "Conditional";
  global_config?: {
    model: string;
    temperature: number;
  };
}

interface Agent {
  name: string;
  role: string;
  tools: string[];
  dependencies?: string[];
  config?: {
    temperature?: number;
    max_tokens?: number;
  };
}
```

---

### 3. Builder Node 👷

**Purpose:** Generate executable Python code from blueprint

**Implementation:**
```python
def builder_node(state: FactoryState) -> dict:
    """
    Builder Agent: Code generation from approved blueprint.
    
    Input from state:
        - current_blueprint: Approved JSON design
    
    Output to state:
        - final_code: Complete Python code
        - status: "finished"
    
    Code Requirements:
        - Uses LangChain & LangGraph
        - Creates StateGraph
        - Defines all agents as nodes
        - Proper imports and error handling
        - Production-ready quality
    """
    print("\n--- 👷 BUILDER IS CODING ---")
    
    # Construct code generation prompt
    prompt = f"""
    You are a Python Expert specializing in LangChain and LangGraph.
    
    Write the complete, executable code for this AI agent system:
    
    Blueprint:
    {state['current_blueprint']}
    
    Requirements:
    - Use `langchain_openai` for LLM integration
    - Use `langgraph` for workflow orchestration
    - Create a StateGraph with proper state management
    - Define nodes for each agent
    - Add edges to connect the workflow
    - Compile the graph
    - Include proper error handling
    - Add comments for clarity
    
    Output ONLY valid Python code. No explanations, no markdown formatting.
    Make it production-ready and well-structured.
    """
    
    # Invoke LLM
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Clean markdown code fencing
    code = response.content.replace("```python", "").replace("```", "").strip()
    
    return {
        "final_code": code,
        "status": "finished"
    }
```

**Generated Code Template:**
```python
# ============================================================================
# AUTO-GENERATED LANGCHAIN AGENT SYSTEM
# Generated by Meta-Agent Factory (LangChain Version)
# ============================================================================

import os
from typing import TypedDict, Optional, List
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

# Load environment variables
load_dotenv()

# Validate API key
if "OPENAI_API_KEY" not in os.environ:
    raise RuntimeError("OPENAI_API_KEY not found")

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# ============================================================================
# STATE DEFINITION
# ============================================================================

class SystemState(TypedDict):
    """State for the agent system."""
    input: str
    output: str
    intermediate_results: List[str]

# ============================================================================
# AGENT NODES
# ============================================================================

def agent1_node(state: SystemState) -> dict:
    """First agent in the pipeline."""
    # Agent logic here
    return {"intermediate_results": [result]}

def agent2_node(state: SystemState) -> dict:
    """Second agent in the pipeline."""
    # Agent logic here
    return {"output": final_result}

# ============================================================================
# GRAPH CONSTRUCTION
# ============================================================================

workflow = StateGraph(SystemState)

# Add nodes
workflow.add_node("agent1", agent1_node)
workflow.add_node("agent2", agent2_node)

# Add edges
workflow.set_entry_point("agent1")
workflow.add_edge("agent1", "agent2")
workflow.add_edge("agent2", END)

# Compile
app = workflow.compile()

# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    result = app.invoke({"input": "Test query"})
    print(result["output"])
```

---

## 🕸️ Graph Construction

### StateGraph Setup

```python
from langgraph.graph import StateGraph, END

# Initialize with state type
workflow = StateGraph(FactoryState)

# Add agent nodes
workflow.add_node("consultant", consultant_node)
workflow.add_node("architect", architect_node)
workflow.add_node("builder", builder_node)

# Set entry point
workflow.set_entry_point("consultant")

# Add edges
workflow.add_edge("consultant", END)  # Pause for human input
workflow.add_edge("architect", END)   # Pause for approval
workflow.add_edge("builder", END)     # Complete

# Compile into executable app
app = workflow.compile()
```

### Why END Instead of Conditional Edges?

**Our Approach:**
```python
workflow.add_edge("consultant", END)
# Then manually: app.invoke(state)
```

**Alternative (Fully Automated):**
```python
workflow.add_conditional_edges(
    "consultant",
    router_function,
    {
        "architect": "architect",
        "end": END
    }
)
```

**Why We Use END:**
- ✅ Human input required between phases
- ✅ More control over execution flow
- ✅ Clear checkpoints for verification
- ✅ Better debugging experience

---

## 🎮 Interactive Execution

### Complete Workflow

```python
# ============================================================================
# PHASE 1: CONSULTATION
# ============================================================================

# Initialize state
state = {
    "user_initial_request": "I want a YouTube script writer agent."
}

# Run consultant
for output in app.stream(state):
    if 'consultant' in output:
        state.update(output['consultant'])

# Display options
print(state['consultant_options'])

# Get user choice
choice = input("Choose strategy: ")
state["user_strategy_choice"] = choice

# ============================================================================
# PHASE 2: ARCHITECTURE (with revision loop)
# ============================================================================

# Run architect
output = app.invoke(state, config={"configurable": {"thread_id": "1"}})
state.update(output)

# Verification loop
iteration = 1
while True:
    print(f"Blueprint (Iteration {iteration}):")
    print(state['current_blueprint'])
    
    feedback = input("Approve or provide feedback: ")
    
    if feedback.lower() == "approved":
        state["status"] = "approved"
        break
    else:
        state["status"] = "revision_requested"
        state["user_feedback"] = feedback
        
        # Re-run architect
        update = architect_node(state)
        state.update(update)
        iteration += 1

# ============================================================================
# PHASE 3: CODE GENERATION
# ============================================================================

# Run builder
update = builder_node(state)
state.update(update)

# Display and save
print(state['final_code'])

with open("generated_langchain_agent.py", "w") as f:
    f.write(state['final_code'])
```

---

## 🔄 Execution Methods

### 1. **Stream Execution**

```python
# Streaming: Get updates as they happen
for output in app.stream(state):
    if 'node_name' in output:
        # Process update
        state.update(output['node_name'])
        print(f"Node completed: {output}")
```

**Use Cases:**
- Real-time progress updates
- Long-running operations
- User feedback during execution

### 2. **Invoke Execution**

```python
# Synchronous: Wait for completion
result = app.invoke(state, config={"configurable": {"thread_id": "1"}})
state.update(result)
```

**Use Cases:**
- Simple workflows
- When streaming not needed
- Batch processing

### 3. **Async Execution**

```python
# Asynchronous: Non-blocking
result = await app.ainvoke(state)
```

**Use Cases:**
- Concurrent workflows
- Web applications
- High-throughput systems

---

## 🔧 Configuration & Customization

### Environment Variables

```bash
# Required
OPENAI_API_KEY=sk-proj-your_key_here

# Optional
GPT_MODEL=gpt-4o
TEMPERATURE=0
MAX_TOKENS=2000
```

### Model Configuration

```python
from langchain_openai import ChatOpenAI

# Basic configuration
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=2000
)

# Advanced configuration
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=2000,
    model_kwargs={
        "top_p": 0.9,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5
    },
    request_timeout=60,
    max_retries=3
)
```

### Switching LLM Providers

```python
# OpenAI (default)
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o")

# Anthropic Claude
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-3-sonnet-20240229")

# Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Ollama (local)
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")
```

---

## 🐛 Debugging & Troubleshooting

### Common Issues

#### 1. Environment Variable Not Found

**Symptom:** "❌ API Key NOT found in .env"

**Solutions:**
```python
# 1. Check .env file exists
import os
print(os.path.exists(".env"))

# 2. Check file contents
with open(".env") as f:
    print(f.read())

# 3. Force reload
from dotenv import load_dotenv
load_dotenv(override=True)

# 4. Restart Jupyter kernel
# Kernel → Restart
```

#### 2. Kernel Caching Issues

**Symptom:** Old values persist after editing .env

**Solution:**
```python
# Always use override=True in notebooks
load_dotenv(override=True)

# Or clear environment manually
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]
load_dotenv()

# Best practice: Restart kernel after .env changes
```

#### 3. Graph Execution Stuck

**Symptom:** Workflow doesn't progress

**Solutions:**
```python
# 1. Check state status
print(f"Current status: {state.get('status')}")

# 2. Verify END conditions
if state["status"] == "waiting_for_approval":
    print("Waiting for user approval - manually update status")

# 3. Add timeout
import asyncio
try:
    result = await asyncio.wait_for(
        app.ainvoke(state),
        timeout=60
    )
except asyncio.TimeoutError:
    print("Execution timed out")
```

---

## 📊 Performance Optimization

### 1. **Batch Processing**

```python
# Process multiple requests in parallel
import asyncio

async def process_multiple(requests: List[str]):
    tasks = [
        app.ainvoke({"user_initial_request": req})
        for req in requests
    ]
    results = await asyncio.gather(*tasks)
    return results

# Usage
requests = ["Build agent 1", "Build agent 2", "Build agent 3"]
results = await process_multiple(requests)
```

### 2. **Caching**

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_llm_response(prompt: str) -> str:
    """Cache LLM responses for repeated prompts."""
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
```

### 3. **Streaming for Long Operations**

```python
# Stream tokens for better UX
for chunk in llm.stream("Long prompt..."):
    print(chunk.content, end="", flush=True)
```

---

## 🧪 Testing

### Unit Tests

```python
import unittest
from unittest.mock import Mock, patch

class TestConsultantNode(unittest.TestCase):
    def test_consultant_returns_options(self):
        state = {"user_initial_request": "Test request"}
        result = consultant_node(state)
        
        self.assertIn("consultant_options", result)
        self.assertEqual(result["status"], "waiting_for_user_strategy")
    
    def test_consultant_with_empty_request(self):
        state = {"user_initial_request": ""}
        with self.assertRaises(ValueError):
            consultant_node(state)
```

### Integration Tests

```python
def test_full_workflow():
    """Test complete agent factory pipeline."""
    state = {"user_initial_request": "Build test agent"}
    
    # Phase 1
    output = app.invoke(state)
    assert "consultant_options" in output
    
    # Phase 2
    state.update(output)
    state["user_strategy_choice"] = "Option 1"
    output = app.invoke(state)
    assert "current_blueprint" in output
    
    # Phase 3
    state.update(output)
    state["status"] = "approved"
    output = builder_node(state)
    assert "final_code" in output
```

---

## 📚 Best Practices

### 1. **State Management**
- ✅ Use TypedDict for type safety
- ✅ Keep state minimal (only essential fields)
- ✅ Document each field clearly
- ✅ Validate state transitions

### 2. **Node Design**
- ✅ Single responsibility per node
- ✅ Pure functions (no side effects)
- ✅ Return only state updates (not full state)
- ✅ Handle errors gracefully

### 3. **Prompt Engineering**
- ✅ Be specific and detailed
- ✅ Include constraints explicitly
- ✅ Provide examples when possible
- ✅ Test with edge cases

### 4. **Error Handling**
- ✅ Validate inputs before LLM calls
- ✅ Catch and log API errors
- ✅ Provide user-friendly error messages
- ✅ Implement retry logic

---

## 🔗 Related Documentation

- [Google ADK Version Documentation](./GOOGLE_ADK_VERSION.md)
- [Main README](../README.md)
- [LangChain Docs](https://python.langchain.com/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)

---

**Last Updated:** December 10, 2025
