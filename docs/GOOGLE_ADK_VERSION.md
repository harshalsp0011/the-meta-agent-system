# 🔵 Google ADK Version - Detailed Documentation

## 📋 Overview

This document provides in-depth technical documentation for the **Google Agent Development Kit (ADK)** implementation of the Meta-Agent Factory System.

**File Location:** `src/root.ipynb`

---

## 🏗️ Architecture Deep Dive

### System Components

#### 1. **Storage Manager** 💾

**Purpose:** Persistent storage for blueprints and generated code

**Implementation:**
```python
class StorageManager:
    def __init__(self, base_dir: str = "agent_factory_storage"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
    
    def save_blueprint(self, agent_name: str, blueprint: dict) -> Path
    def load_blueprint(self, agent_name: str) -> dict
    def save_agent_code(self, agent_name: str, code: str) -> Path
    def load_agent_code(self, agent_name: str) -> str
    def list_agents(self) -> List[str]
```

**Storage Structure:**
```
agent_factory_storage/
├── {agent_name}/
│   ├── blueprint.json    # JSON system design
│   └── agent.py          # Generated Python code
```

**Key Features:**
- ✅ Automatic directory creation
- ✅ JSON serialization/deserialization
- ✅ Error handling for missing files
- ✅ Agent discovery and listing

---

#### 2. **Consultant Agent** 🤔

**Role:** Requirements clarification and strategy proposal

**Configuration:**
```python
consultant_agent = Agent(
    name="Consultant",
    model=get_gemini_model(),
    instruction="""
    You are an AI Solutions Consultant specializing in multi-agent system design.
    
    Your task:
    1. Analyze the user's request
    2. Propose 2-3 distinct architectural approaches
    3. Explain trade-offs for each option
    4. Help user choose the best strategy
    
    Options should vary in complexity:
    - Simple: Fast MVP, fewer components
    - Moderate: Balanced approach
    - Complex: Full-featured, production-ready
    
    Present options clearly with pros/cons.
    """,
    tools=[clarification_tool]  # Optional: ask follow-up questions
)
```

**Interaction Flow:**
```
User Input → Consultant Agent → 2-3 Options → User Selection → Next Phase
```

**Output Format:**
```
Option 1: [Simple Approach]
- Description: ...
- Agents: ...
- Pros: ...
- Cons: ...

Option 2: [Moderate Approach]
...

Option 3: [Complex Approach]
...
```

---

#### 3. **Architect Agent** 📐

**Role:** System blueprint design with iterative refinement

**Configuration:**
```python
architect_agent = Agent(
    name="Architect",
    model=get_gemini_model(),
    instruction="""
    You are a Systems Architect for multi-agent AI systems.
    
    Design a JSON blueprint based on the user's chosen strategy.
    
    Blueprint Structure:
    {
      "system_name": "snake_case_name",
      "description": "What this system does",
      "flow_type": "Sequential" | "Parallel" | "Conditional",
      "agents": [
        {
          "name": "AgentName",
          "role": "What this agent does",
          "tools": ["tool1", "tool2"],
          "dependencies": ["other_agent"]  // Optional
        }
      ]
    }
    
    Ensure:
    - Clear agent responsibilities
    - Minimal overlap between agents
    - Proper tool selection
    - Logical workflow
    
    Output ONLY valid JSON.
    """,
    tools=[blueprint_verification_tool]
)
```

**Verification Loop:**
```python
while not user_approved:
    blueprint = architect_agent.generate_blueprint(strategy)
    user_feedback = await get_user_approval(blueprint)
    
    if user_feedback == "approved":
        break
    else:
        # Incorporate feedback and regenerate
        architect_agent.refine_blueprint(blueprint, user_feedback)
```

**Blueprint Schema:**
```json
{
  "system_name": "string (required)",
  "description": "string (required)",
  "flow_type": "Sequential | Parallel | Conditional",
  "agents": [
    {
      "name": "string (required)",
      "role": "string (required)",
      "tools": ["array of strings"],
      "dependencies": ["array of agent names"],
      "config": {
        "temperature": 0.7,
        "max_tokens": 1000
      }
    }
  ],
  "global_config": {
    "model": "gemini-2.5-flash-lite",
    "timeout": 30
  }
}
```

---

#### 4. **Builder Agent** 👷

**Role:** Python code generation from approved blueprint

**Configuration:**
```python
builder_agent = Agent(
    name="Builder",
    model=get_gemini_model(),
    instruction="""
    You are a Python Expert specializing in Google Agent Development Kit (ADK).
    
    Generate production-ready Python code from the given JSON blueprint.
    
    STRICT REQUIREMENTS:
    ✅ MUST import: google.generativeai, google.adk
    ✅ MUST use: Agent, Tool, SequentialFlow / ParallelFlow
    ✅ MUST define: root_agent variable as the main entry point
    ✅ MUST include: Proper type hints (from typing)
    ✅ MUST add: Docstrings for all functions and classes
    
    ❌ NEVER hardcode: API keys or secrets
    ❌ NEVER use: Deprecated packages
    ❌ NEVER import: Unnecessary libraries
    
    Code Structure:
    1. Imports
    2. Tool definitions (if needed)
    3. Agent definitions
    4. Flow composition
    5. root_agent = ... (main agent)
    
    Output ONLY Python code. No explanations, no markdown.
    """,
    tools=[syntax_validator_tool]
)
```

**Code Generation Process:**
```python
def generate_code(blueprint: dict) -> str:
    # Parse blueprint
    agents = blueprint["agents"]
    flow_type = blueprint["flow_type"]
    
    # Generate imports
    code = generate_imports()
    
    # Generate tool definitions
    for agent in agents:
        if agent.get("tools"):
            code += generate_tools(agent["tools"])
    
    # Generate agent definitions
    for agent in agents:
        code += generate_agent(agent)
    
    # Generate flow composition
    code += generate_flow(agents, flow_type)
    
    # Validate syntax
    validate_syntax(code)
    
    return code
```

**Generated Code Template:**
```python
# ============================================================================
# AUTO-GENERATED AGENT SYSTEM
# Generated by Meta-Agent Factory System
# Blueprint: {system_name}
# ============================================================================

import os
from typing import Optional, List, Dict
import google.generativeai as genai
from google.adk import Agent, Tool, SequentialFlow

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ============================================================================
# TOOL DEFINITIONS
# ============================================================================

def tool_name(param: str) -> str:
    """Tool description."""
    # Implementation
    return result

# ============================================================================
# AGENT DEFINITIONS
# ============================================================================

agent_1 = Agent(
    name="AgentName",
    model="gemini-2.5-flash-lite",
    instruction="Agent instructions...",
    tools=[tool_name]
)

# ============================================================================
# FLOW COMPOSITION
# ============================================================================

root_agent = SequentialFlow(
    agents=[agent_1, agent_2],
    name="SystemName"
)

# ============================================================================
# EXECUTION (Optional)
# ============================================================================

if __name__ == "__main__":
    response = root_agent.run("Test query")
    print(response)
```

---

#### 5. **Dynamic Executor** ⚡

**Role:** Runtime loading and execution of generated agents

**Implementation:**
```python
import importlib.util
import sys
from pathlib import Path

def load_and_run_agent(agent_name: str, query: str):
    """
    Dynamically load generated agent and execute query.
    
    Args:
        agent_name: Name of the agent (folder name)
        query: User query to process
        
    Returns:
        Agent response
    """
    # Construct path to generated agent
    agent_path = Path(f"agent_factory_storage/{agent_name}/agent.py")
    
    if not agent_path.exists():
        raise FileNotFoundError(f"Agent not found: {agent_name}")
    
    # Load module dynamically
    spec = importlib.util.spec_from_file_location(
        f"agent_{agent_name}",
        agent_path
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    
    # Get root_agent from module
    if not hasattr(module, "root_agent"):
        raise AttributeError(f"No 'root_agent' found in {agent_name}/agent.py")
    
    root_agent = module.root_agent
    
    # Execute query
    response = root_agent.run(query)
    
    return response
```

**Key Benefits:**
- ✅ No kernel restart needed
- ✅ Instant testing after generation
- ✅ Module isolation (each agent in separate namespace)
- ✅ Error handling for missing attributes

---

## 🔄 Complete Workflow

### End-to-End Process

```python
async def run_agent_factory(
    user_initial_prompt: str,
    agent_name_slug: str
) -> str:
    """
    Complete agent factory pipeline.
    
    Phases:
    1. Consultation - Strategy selection
    2. Architecture - Blueprint design with approval loop
    3. Build - Code generation and storage
    4. Execute - Dynamic loading and testing
    
    Returns:
        agent_id: Identifier for the generated agent
    """
    
    # Initialize storage
    storage = StorageManager()
    
    # ========================================================================
    # PHASE 1: CONSULTATION
    # ========================================================================
    print("🔵 Phase 1: Consultation")
    
    # Consultant proposes options
    options = await consultant_agent.run(user_initial_prompt)
    print(f"Options:\n{options}")
    
    # User selects strategy
    user_choice = input("Choose option (1/2/3): ")
    strategy = f"Option {user_choice} from: {options}"
    
    # ========================================================================
    # PHASE 2: ARCHITECTURE (with verification loop)
    # ========================================================================
    print("\n🔵 Phase 2: Architecture Design")
    
    approved = False
    blueprint = None
    
    while not approved:
        # Generate blueprint
        blueprint_str = await architect_agent.run(
            f"Strategy: {strategy}\nOriginal request: {user_initial_prompt}"
        )
        
        # Parse JSON
        blueprint = json.loads(blueprint_str)
        
        # Show to user
        print(f"\nProposed Blueprint:")
        print(json.dumps(blueprint, indent=2))
        
        # Get approval
        feedback = input("\nApprove? (yes/no or provide feedback): ")
        
        if feedback.lower() in ["yes", "approved", "y"]:
            approved = True
            print("✅ Blueprint approved!")
        else:
            print(f"🔄 Refining based on feedback: {feedback}")
            # Add feedback to next iteration
            strategy += f"\n\nUser feedback: {feedback}"
    
    # Save approved blueprint
    storage.save_blueprint(agent_name_slug, blueprint)
    
    # ========================================================================
    # PHASE 3: BUILD
    # ========================================================================
    print("\n🔵 Phase 3: Code Generation")
    
    # Generate code
    code = await builder_agent.run(
        f"Generate Python code for this blueprint:\n{json.dumps(blueprint)}"
    )
    
    # Validate syntax
    try:
        compile(code, "<string>", "exec")
        print("✅ Code syntax validated")
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        # Could loop back to Builder with error message
    
    # Save code
    storage.save_agent_code(agent_name_slug, code)
    print(f"💾 Code saved to: agent_factory_storage/{agent_name_slug}/agent.py")
    
    # ========================================================================
    # PHASE 4: EXECUTE (Optional Test)
    # ========================================================================
    print("\n🔵 Phase 4: Testing")
    
    test_query = input("Enter test query (or skip): ")
    if test_query:
        try:
            result = load_and_run_agent(agent_name_slug, test_query)
            print(f"\n✅ Agent Response:\n{result}")
        except Exception as e:
            print(f"❌ Execution error: {e}")
    
    return agent_name_slug
```

---

## ⚙️ Configuration & Customization

### Environment Variables

```bash
# Required
GOOGLE_API_KEY=your_api_key_here

# Optional (with defaults)
GEMINI_MODEL=gemini-2.5-flash-lite
FACTORY_STORAGE_PATH=agent_factory_storage
MAX_REFINEMENT_ITERATIONS=5
BUILDER_TEMPERATURE=0
CONSULTANT_TEMPERATURE=0.7
```

### Dynamic Model Loading

```python
def get_gemini_model():
    """Get configured Gemini model from environment."""
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
    return model_name

# Usage in agent definitions
consultant_agent = Agent(
    name="Consultant",
    model=get_gemini_model(),  # Dynamically loaded
    instruction="..."
)
```

### Custom Tool Integration

```python
# Define custom tool
def custom_search(query: str) -> str:
    """Custom search implementation."""
    # Your logic here
    return results

# Add to Builder's instructions
builder_agent.instruction += """
Available custom tools:
- custom_search(query: str) -> str: Searches custom database

Use these tools when appropriate in generated agents.
"""
```

---

## 🔍 Debugging & Troubleshooting

### Common Issues

#### 1. Blueprint Not Approved
**Symptom:** Infinite loop in architect phase

**Solution:**
```python
# Add iteration counter
max_iterations = 5
iteration = 0

while not approved and iteration < max_iterations:
    # ... blueprint generation ...
    iteration += 1

if iteration >= max_iterations:
    print("⚠️ Max iterations reached. Using last blueprint.")
    approved = True
```

#### 2. Generated Code Has Syntax Errors
**Symptom:** `compile()` fails during validation

**Solution:**
```python
# Add detailed error reporting
try:
    compile(code, "<string>", "exec")
except SyntaxError as e:
    print(f"Line {e.lineno}: {e.msg}")
    print(f"Text: {e.text}")
    
    # Send back to Builder with error context
    code = await builder_agent.run(
        f"Fix this syntax error:\n{e}\n\nOriginal code:\n{code}"
    )
```

#### 3. Dynamic Executor Can't Find `root_agent`
**Symptom:** `AttributeError: module has no attribute 'root_agent'`

**Solution:**
```python
# Validate generated code has root_agent
if "root_agent" not in code:
    print("❌ Generated code missing 'root_agent' variable")
    # Add to Builder's next generation
    builder_agent.instruction += "\n\nIMPORTANT: Always define 'root_agent' as the main entry point!"
```

---

## 📊 Performance Optimization

### API Call Reduction

```python
# Cache model instances
_model_cache = {}

def get_cached_model(model_name: str):
    if model_name not in _model_cache:
        _model_cache[model_name] = genai.GenerativeModel(model_name)
    return _model_cache[model_name]
```

### Parallel Agent Execution

```python
# Use asyncio for parallel consultation/architecture
async def parallel_agents(blueprint):
    tasks = [
        architect_agent.run_async(prompt1),
        builder_agent.run_async(prompt2)
    ]
    results = await asyncio.gather(*tasks)
    return results
```

---

## 🧪 Testing Generated Agents

### Unit Testing Framework

```python
import unittest

class TestGeneratedAgent(unittest.TestCase):
    def setUp(self):
        self.agent = load_agent("personal_shopper")
    
    def test_agent_response(self):
        response = self.agent.run("Find laptops under $1000")
        self.assertIsNotNone(response)
        self.assertIn("laptop", response.lower())
    
    def test_agent_error_handling(self):
        response = self.agent.run("")
        self.assertIn("error", response.lower())
```

---

## 📚 Best Practices

### 1. **Prompt Engineering**
- Be specific in agent instructions
- Include examples of good outputs
- Add constraints and rules explicitly

### 2. **Error Handling**
- Always validate JSON blueprints
- Compile-check generated code
- Handle API rate limits gracefully

### 3. **Security**
- Never hardcode API keys
- Validate user input before passing to agents
- Sanitize generated code before execution

### 4. **Versioning**
- Save blueprint versions with timestamps
- Track changes to agent instructions
- Maintain changelog for generated agents

---

## 🔗 Related Documentation

- [LangChain Version Documentation](./LANGCHAIN_VERSION.md)
- [Main README](../README.md)
- [Google ADK Official Docs](https://github.com/google/generative-ai-python)

---

**Last Updated:** December 10, 2025
