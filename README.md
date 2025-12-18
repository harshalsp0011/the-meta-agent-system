# The Meta Agent Factory System

> **Build AI Agent Systems with AI, not code.**
>
> A meta-agent system that uses multiple specialized AI agents to automatically design and generate multi-agent systems.
## 📚 Documentation

**Main Documentation:**
- [📖 README (This File)](#) - Quick start and overview
- [🔵 Google ADK Version - Detailed Guide](./docs/GOOGLE_ADK_VERSION.md) - In-depth Google ADK implementation
- [ LangChain Version - Detailed Guide](./docs/LANGCHAIN_VERSION.md) - In-depth LangChain implementation

**Quick Navigation:**
- [Problem Statement](#-problem-statement)
- [What This System Can Do](#-what-this-system-can-do)
- [Architecture & Technology](#️-how-we-build-it---the-architecture)
- [Quick Start](#-quick-start)
- [Skills & Technologies](#-skills--technologies-used)
- [Usage Examples](#-usage-examples)

---

## Skills & Technologies Used

### AI & Machine Learning
- **Large Language Models (LLMs)**: Google Gemini, OpenAI GPT-4o
- **Prompt Engineering**: Advanced prompt design and optimization
- **Multi-Agent Systems**: Agent orchestration and coordination
- **Agentic AI**: Autonomous agent design patterns

### 💻 Frameworks & Libraries
- **Google Agent Development Kit (ADK)**: Production-ready agent framework
- **LangChain**: LLM application framework and tooling
- **LangGraph**: Stateful agent workflow orchestration
- **Pydantic**: Data validation and type safety

### Python Development
- **Async Programming**: `asyncio`, `aiosqlite` for concurrent operations
- **Dynamic Code Execution**: `importlib` for runtime module loading
- **Type Hints**: Advanced typing with `TypedDict`, generics
- **Environment Management**: `python-dotenv` for configuration

### Software Architecture
- **Design Patterns**: Strategy, Factory, Observer patterns
- **Separation of Concerns**: Modular, single-responsibility components
- **Human-in-the-Loop (HITL)**: Interactive AI systems with verification
- **State Management**: Stateful workflow design

### Development Practices
- **Jupyter Notebooks**: Interactive development and documentation
- **Version Control**: Git workflow and collaborative development
- **Code Generation**: Automated Python code synthesis
- **Testing & Validation**: Syntax validation, error handling

### Data & Storage
- **JSON Schema Design**: Blueprint structure and validation
- **File System Management**: Persistent storage strategies
- **SQLAlchemy**: (Optional) Database integration

### Security & Best Practices
- **API Key Management**: Secure credential handling
- **Environment Variables**: Configuration separation
- **Input Validation**: Sanitization and error checking
- **Code Safety**: Sandboxed execution patterns

---


### Key Capabilities at a Glance

```
INPUT: "Build me a shopping agent"
 ↓
CONSULTANT: Proposes options
 ↓
ARCHITECT: Designs blueprint with your approval
 ↓
BUILDER: Generates production Python code
 ↓
EXECUTOR: Runs your agent immediately
 ↓
OUTPUT: Ready-to-use agent system
```

**Time to agent:** Minutes instead of days 
**Code written by:** AI, not humans 
**Quality assured by:** Human feedback loops 
**Ready to deploy:** Instantly

## Problem Statement

Building multi-agent systems is **complex, time-consuming, and error-prone**:

- Requires deep knowledge of frameworks and APIs
- Lots of boilerplate code to write and maintain
- Changes mean rewriting entire systems
- Hard to iterate and experiment with different architectures

**This system solves that by:**

 Using AI agents to design and build other agents 
 Automating code generation from simple descriptions 
 Including human-in-the-loop verification 
 Enabling rapid iteration and experimentation 

---

## What This System Can Do

### Agent Generation Capabilities

This system can automatically generate AI agents for:

**🛒 E-Commerce & Shopping**
- Price comparison across multiple stores
- Shopping assistants with cart management
- Deal hunters and bargain trackers
- Product recommendation engines

**📧 Communication & Automation**
- Email management and filtering agents
- Chatbots for customer support
- Social media content schedulers
- Notification orchestrators

** Data & Analytics**
- Data processing pipelines
- Report generation systems
- Analytics dashboards coordinators
- Data validation agents

**🔍 Search & Discovery**
- Web search integrators
- Document retrieval systems
- Content recommendation engines
- Knowledge base assistants

**💼 Business Processes**
- Workflow automation agents
- Task scheduling coordinators
- Approval workflow managers
- Lead qualification agents

**And many more!** The system is flexible enough to design any multi-agent architecture you can describe.

---

## How We Build It - The Architecture

### The Building Process

**Step 1: You Describe What You Want**
```
User Input: "I want a shopping agent that finds products and buys them"
```

**Step 2: Consultant Clarifies & Proposes**
- Consultant Agent receives your vague request
- Analyzes and proposes 2-3 specific architectural approaches
- You choose which direction you want (Option 1, 2, or 3)
- Consultant sends your strategic choice forward

**Step 3: Architect Designs with Your Approval**
- Architect Agent receives refined requirements
- Generates a JSON blueprint (system design)
- Shows you the design
- You can approve or request changes
- If changes needed, architect iteratively refines until approved
- Final blueprint is saved

**Step 4: Builder Generates Python Code**
- Builder Agent receives approved JSON blueprint
- Generates complete, executable Python code using Google ADK
- Code includes all agents, tools, and configurations
- Enforces strict quality rules (no hardcoded keys, proper imports, etc.)
- Code is saved as `agent.py`

**Step 5: Executor Runs Your Agent**
- Dynamic loader imports the generated code
- Agent is instantiated and ready to use
- You can immediately test with queries
- No kernel restart needed!

### The Technology Stack

**What We Use:**

| Component | Technology | Why |
|-----------|-----------|-----|
| **Framework** | Google Agent Development Kit (ADK) | Production-ready, type-safe, best practices |
| **LLM** | Google Gemini API | Fast, reliable, supports tool use |
| **Code Generation** | Prompt Engineering + Validation | Ensures quality, enforces rules |
| **Storage** | JSON + Python Files | Version control friendly, portable |
| **Execution** | Python `importlib` | Dynamic loading, fast iteration |
| **Development** | Jupyter Notebook | Interactive, easy debugging |
| **Config** | Python-dotenv | Secure, environment-based secrets |

**Libraries Used:**
```python
google-genai # Gemini API client
google-adk # Agent Development Kit
python-dotenv # Environment configuration
aiosqlite, asyncio # Async support
pydantic # Data validation
sqlalchemy # Optional: for data persistence
```

**Key Design Patterns:**
- **Multi-Agent Pattern:** Specialist agents for each phase
- **Iterative Refinement:** Loop until user approval
- **Tool Use:** Agents have tools to complete tasks
- **Sequential & Parallel Flows:** Flexible agent composition
- **Dynamic Loading:** Instant execution without restart

### Why This Approach?

**Why 3 Specialist Agents instead of 1 mega-agent?**
- Each agent is expert in its domain (strategy, design, coding)
- Better quality outputs through specialization
- Easier to debug and improve each phase
- Clearer feedback loops for human oversight

**Why JSON Blueprints?**
- Language-agnostic (can generate Python, JS, Go, etc.)
- Easy to version control and track changes
- Human-readable design documentation
- Can be validated before code generation

**Why Iterative Feedback Loop?**
- User ensures design matches their intent
- Catches problems before coding
- Enables customization without code changes
- Builds trust in AI-generated systems

**Why Dynamic Execution?**
- No kernel restart = fast iteration
- Test changes instantly
- Better developer experience
- Enables live debugging

**Why Google ADK?**
- Production-ready framework
- Type-safe agent definitions
- Built-in tool handling
- Support for both Sequential and Parallel flows
- Active development and support

---

## Quick Start

### Prerequisites
```bash
python >= 3.10
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite # or any other supported model
```

### Run the System
```bash
# Open and run the Jupyter notebook
jupyter notebook src/root.ipynb

# Follow the interactive prompts to build your agent
```

### Quick Example
```python
# In the notebook, simply run:
agent_id = await run_agent_factory(
 user_initial_prompt="I want a shopping agent that finds products and buys them.",
 agent_name_slug="personal_shopper"
)

# The system will:
# 1. Consultant analyzes your request
# 2. Architect designs the blueprint
# 3. You approve the design
# 4. Builder generates Python code
# 5. Agent is automatically tested

# Your agent is now ready at:
# agent_factory_storage/personal_shopper/agent.py
```

---

## System Architecture Overview

The system consists of **5 key components** working in a 3-phase pipeline:

```
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: STRATEGY │
│ CONSULTANT AGENT analyzes │
│ user request & proposes solutions │
└────────────────────┬────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: DESIGN │
│ ARCHITECT AGENT designs blueprints │
│ with iterative human feedback loops │
└────────────────────┬────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: BUILD │
│ BUILDER AGENT generates Python code │
│ STORAGE MANAGER persists outputs │
│ DYNAMIC EXECUTOR runs the new agent │
└─────────────────────────────────────────────────────────┘
```

---

## System Architecture

### Overview
The system consists of **5 key components** working in a 3-phase pipeline:

```
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: STRATEGY │
│ CONSULTANT AGENT analyzes │
│ user request & proposes solutions │
└────────────────────┬────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: DESIGN │
│ ARCHITECT AGENT designs blueprints │
│ with iterative human feedback loops │
└────────────────────┬────────────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: BUILD │
│ BUILDER AGENT generates Python code │
│ STORAGE MANAGER persists outputs │
│ DYNAMIC EXECUTOR runs the new agent │
└─────────────────────────────────────────────────────────┘
```

### Components

#### 1. **Consultant Agent** 
**Role:** Strategy & Requirements Clarification

- Takes vague user requests
- Proposes 2-3 specific architectural approaches
- Collects user's strategic choice
- Ensures clarity before design phase

**Example:**
```
User: "I want a shopping agent"

Consultant proposes:
1. Deal Hunter - searches prices only
2. Full Concierge - search, cart, checkout
3. Price Tracker - monitors prices over time

User chooses: Option 2
```

#### 2. **Architect Agent** 
**Role:** System Blueprint Design

- Receives refined requirements from Consultant
- Proposes JSON blueprint for multi-agent system
- **Pauses for human feedback** (verification tool)
- Iteratively refines until approved
- Generates final JSON blueprint

**Blueprint structure:**
```json
{
 "system_name": "personal_shopper",
 "description": "Finds products and completes purchases",
 "flow_type": "Sequential",
 "agents": [
 {
 "name": "SearchAgent",
 "role": "Search for products matching criteria",
 "tools": ["search"]
 },
 {
 "name": "CartAgent",
 "role": "Manage shopping cart",
 "tools": ["add_to_cart", "remove_from_cart"]
 },
 {
 "name": "CheckoutAgent",
 "role": "Complete purchase",
 "tools": ["checkout"]
 }
 ]
}
```

#### 3. **Builder Agent** 
**Role:** Code Generation

- Receives approved JSON blueprint
- Generates **production-ready Python code** using Google ADK
- Enforces strict syntax and import rules
- Validates all agent definitions

**Enforces:**
- Only approved imports from Google ADK
- Proper agent configuration with model & tools
- Valid JSON blueprint structure
- No hardcoded secrets or API keys
- No deprecated packages

#### 4. **Storage Manager** 
**Role:** Persistent Storage

- Saves blueprints as JSON files
- Saves generated code as Python files
- Organizes agents by name in `agent_factory_storage/`

**Directory structure:**
```
agent_factory_storage/
├── personal_shopper/
│ ├── blueprint.json # System design
│ └── agent.py # Generated code
├── email_assistant/
│ ├── blueprint.json
│ └── agent.py
└── ...
```

#### 5. **Dynamic Executor** 
**Role:** Runtime Execution

- Dynamically loads generated `.py` files using `importlib`
- Instantiates and runs agents without kernel restart
- Enables iterative development & testing

---

## Data Flow

### End-to-End Workflow

```
1. USER INPUT
 ↓
 "I want a shopping agent"
 
2. CONSULTANT PHASE
 ├─ Receives: User prompt
 ├─ Outputs: 2-3 options
 └─ Result: User selects Option 2
 
3. ARCHITECT PHASE
 ├─ Loop:
 │ ├─ Design blueprint
 │ ├─ Show to user
 │ ├─ Get feedback
 │ └─ Refine or approve
 └─ Result: Final JSON blueprint
 
4. BUILDER PHASE
 ├─ Receives: Blueprint JSON
 ├─ Generates: Python code
 └─ Result: Executable agent
 
5. STORAGE PHASE
 ├─ Saves: blueprint.json
 └─ Saves: agent.py
 
6. EXECUTION PHASE
 ├─ Loads: Generated agent
 ├─ Runs: With user query
 └─ Result: Agent output
```

---

## Usage Examples

### Example 1: Build a Price Comparison Agent

```
Prompt: "I want an agent that compares prices across stores"

Consultant suggests:
1. Simple Scraper - just fetches prices
2. Smart Aggregator - scrapes + finds best deals
3. Full Platform - compare, recommend, track

User chooses: Option 2

Architect designs:
- ScraperAgent (searches multiple stores)
- PriceAnalyzer (finds best deal)
- RecommendationEngine (suggests products)

Builder generates:
- Sequential flow: Scraper → Analyzer → Recommender
- Each agent properly configured with tools
- Ready-to-run Python code

Result: agent_factory_storage/price_comparator/agent.py
```

### Example 2: Iterate on Existing Agent

```
User: "Add a verification step before checkout"

System loads existing blueprint
Architect adds verification agent
User approves new design
Builder generates updated code
Agent is redeployed instantly
```

---

## 🛠️ Configuration

### Environment Variables (`.env`)

```bash
# API Configuration
GOOGLE_API_KEY=your_api_key_here # Required
GEMINI_MODEL=gemini-2.5-flash-lite # Model to use

# Optional
FACTORY_STORAGE_PATH=agent_factory_storage # Where to save agents
LOG_LEVEL=INFO # Logging level
```

### Changing Models

To use a different model:

```bash
# Edit .env
GEMINI_MODEL=gemini-1.5-pro

# Re-run setup cell in notebook
# All agents will automatically use new model
```

---

## 📁 Project Structure

```
the-meta-agent-system/
├── README.md # This file
├── requirements.txt # Python dependencies
├── .env # Configuration (not in git)
│
├── src/
│ └── root.ipynb # Main Jupyter notebook
│ ├── Cell 1: Environment verification
│ ├── Cell 2: Architecture overview + diagrams
│ ├── Cell 3: Core setup & configuration
│ ├── Cell 4: Storage Manager
│ ├── Cell 5: Architect Agent
│ ├── Cell 6: Consultant Agent
│ ├── Cell 7: Builder Agent
│ ├── Cell 8: Orchestrator
│ ├── Cell 9: Dynamic Executor
│ └── Cell 10: Run Factory + Quick Reference
│
├── agent_factory_storage/ # Generated agents (created at runtime)
│ ├── personal_shopper/
│ │ ├── blueprint.json
│ │ └── agent.py
│ └── ...
│
├── info.md # Additional documentation
└── LICENSE # MIT License
```

---

## 🔧 Advanced Usage

## 📚 Implementation Versions

This project includes **two complete implementations** of the same meta-agent factory concept:

### 🔵 [Google ADK Version](./docs/GOOGLE_ADK_VERSION.md)
**File:** `src/root.ipynb`

**Features:**
- Production-ready Google Agent Development Kit
- Google Gemini API integration
- Sequential and Parallel flow support
- Native ADK state management
- Dynamic code execution

**Best For:**
- Production deployments
- Google Cloud integration
- Type-safe agent definitions
- Enterprise applications

**📖 [View Detailed Documentation →](./docs/GOOGLE_ADK_VERSION.md)**

### [LangChain Version](./docs/LANGCHAIN_VERSION.md)
**File:** `src/root_LangChain_version.ipynb`

**Features:**
- LangChain + LangGraph framework
- OpenAI GPT-4o integration
- StateGraph workflow management
- Extensive tool ecosystem
- Multi-provider support

**Best For:**
- Research and experimentation
- Multi-LLM support (OpenAI, Anthropic, etc.)
- Complex workflow patterns
- LangChain ecosystem integration

**📖 [View Detailed Documentation →](./docs/LANGCHAIN_VERSION.md)**

---

## 🔧 Advanced Usage
### Customize Agent Behavior

Edit agent instructions in the notebook:

```python
consultant_agent = Agent(
 name="Consultant",
 model=get_gemini_model(),
 instruction="""
 You are an AI Solutions Consultant.
 [CUSTOMIZE THIS PROMPT]
 """
)
```

### Add Custom Tools

```python
# Define tool function
def custom_search(query: str) -> str:
 """Search for something custom."""
 return f"Results for {query}"

# Add to Builder's instructions
builder_agent.instruction += """
Use custom_search(query) for specific searches
"""
```

### Load Existing Blueprint

```python
# Load from storage
blueprint = storage.load_blueprint("personal_shopper")

# Modify and re-run
# OR pass to architect for iterative improvement
```

---

## 🧪 Testing Generated Agents

After building an agent, test it:

```bash
# Inspect the blueprint
cat agent_factory_storage/personal_shopper/blueprint.json

# Review the code
cat agent_factory_storage/personal_shopper/agent.py

# Run with custom query
# (See notebook cell 10 for execution)
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `GOOGLE_API_KEY not set` | Add to `.env`: `GOOGLE_API_KEY=your_key` |
| `Model not found` | Check model name in `.env`, run setup cell again |
| `Blueprint not saved` | Check JSON syntax in Architect's output |
| `Agent fails to execute` | Ensure blueprint defines `root_agent` variable |
| `Import errors in generated code` | Update Builder's instructions, regenerate |

---

## 📦 What You Get

When you build an agent with this system, you receive:

### Generated Files
```
agent_factory_storage/your_agent_name/
├── blueprint.json # System design document
│ └── Contains: agents, tools, flow type, configuration
└── agent.py # Production Python code
 └── Contains: Agent classes, tools, main execution logic
```

### The Agent
- **Fully functional** - Ready to use immediately
- **Type-safe** - Pydantic models for all inputs/outputs
- **Well-structured** - Clear separation of concerns
- **Documented** - Instructions on what each agent does
- **Tested** - Verified by the Builder agent
- **Modular** - Easy to extend with custom tools

### Development Experience
- **Fast iteration** - Changes in minutes, not hours
- **Human oversight** - You approve each step
- **Clear documentation** - Blueprint explains the design
- **Easy debugging** - Each agent's instructions visible
- **Version tracking** - Blueprint history in JSON

---

## Real-World Comparison

### Traditional Approach (Without This System)
```
Day 1: Analyze requirements
Day 2: Design architecture
Day 3-5: Write boilerplate code
Day 6-7: Implement agents
Day 8: Test and debug
Day 9: Refactor based on feedback
Day 10: Deploy

Total: 2 weeks per agent
```

### With This System
```
Minute 1: Describe what you want
Minute 2: Consultant proposes options
Minute 3: You choose
Minute 4: Architect designs
Minute 5: You approve/refine (loop if needed)
Minute 6: Builder generates code
Minute 7: Agent is ready

Total: 5-10 minutes per agent
```

---

## 📚 Key Concepts

### Why 3 Agents?
- **Separation of Concerns:** Each agent specializes in one task
- **Quality:** Different expertise leads to better outputs
- **Explainability:** Clear what each phase does

### Why Iterative Feedback?
- **User Control:** Ensures output matches intent
- **Quality Assurance:** Problems caught early
- **Customization:** User can guide design choices

### Why Dynamic Loading?
- **Speed:** No kernel restart needed
- **Iteration:** Build → Test → Refine quickly
- **Flexibility:** Agents can be updated without restarting

### Why JSON Blueprints?
- **Language Agnostic:** Can generate code in any language
- **Version Control:** Easy to track design changes
- **Validation:** Schema-based structure ensures correctness

---

## Future Enhancements

- [ ] Export agents as Docker containers
- [ ] Multi-language code generation (Python, JavaScript, Go)
- [ ] Agent marketplace for sharing designs
- [ ] Advanced testing & validation framework
- [ ] Web UI for non-technical users
- [ ] Git integration for blueprint versioning
- [ ] Agent composition & reusability
- [ ] Automatic performance benchmarking

---

## 📖 References

### Official Documentation
- [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-python)
- [Google Gemini API](https://ai.google.dev)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

### Learning Resources
- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [State Management in LangGraph](https://langchain-ai.github.io/langgraph/concepts/state/)
- [Agent Design Patterns](https://python.langchain.com/docs/modules/agents/)

### Project-Specific Documentation
- [🔵 Google ADK Version - Detailed Implementation Guide](./docs/GOOGLE_ADK_VERSION.md)
- [ LangChain Version - Detailed Implementation Guide](./docs/LANGCHAIN_VERSION.md)

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

## 💬 Contributing

Contributions welcome! Areas for improvement:

1. **Agent Design:** Better prompts for consultant/architect/builder
2. **Code Generation:** Stricter validation rules
3. **Testing:** Unit tests for generated agents
4. **Documentation:** More examples and guides
5. **Performance:** Optimize API calls and caching

---

## ❓ FAQ

**Q: Can I use this with other LLMs?** 
A: Currently supports Google Gemini. Adding support for other models is planned.

**Q: What if the generated code doesn't work?** 
A: Architect can be asked to regenerate with feedback, or you can manually fix and re-run.

**Q: How are agents stored?** 
A: Blueprints saved as JSON, code saved as Python files in `agent_factory_storage/`

**Q: Can I modify generated agents?** 
A: Yes! Edit the `.py` files directly or use the factory to regenerate with changes.

**Q: Is this production-ready?** 
A: Great for prototyping and iteration. Production use requires additional testing & validation.

---

## 📧 Questions or Issues?

Open an issue on GitHub or reach out to the maintainers.