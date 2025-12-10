# 🏭 The Meta Agent Factory System

> **Build AI Agent Systems with AI, not code.**
>
> A meta-agent system that uses multiple specialized AI agents to automatically design and generate multi-agent systems.

## 🎯 Problem Statement

Building multi-agent systems is **complex, time-consuming, and error-prone**:

- ❌ Requires deep knowledge of frameworks and APIs
- ❌ Lots of boilerplate code to write and maintain
- ❌ Changes mean rewriting entire systems
- ❌ Hard to iterate and experiment with different architectures

**This system solves that by:**

✅ Using AI agents to design and build other agents  
✅ Automating code generation from simple descriptions  
✅ Including human-in-the-loop verification  
✅ Enabling rapid iteration and experimentation  

---

## 🚀 Quick Start

### Prerequisites
```bash
python >= 3.10
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash-lite  # or any other supported model
```

### Run the System
```bash
# Open and run the Jupyter notebook
jupyter notebook src/root.ipynb

# Follow the interactive prompts to build your agent
```

---

## 🏗️ System Architecture

### Overview
The system consists of **5 key components** working in a 3-phase pipeline:

```
┌─────────────────────────────────────────────────────────┐
│                    PHASE 1: STRATEGY                    │
│              CONSULTANT AGENT analyzes                  │
│            user request & proposes solutions            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                    PHASE 2: DESIGN                      │
│            ARCHITECT AGENT designs blueprints           │
│         with iterative human feedback loops             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                    PHASE 3: BUILD                       │
│          BUILDER AGENT generates Python code            │
│            STORAGE MANAGER persists outputs             │
│        DYNAMIC EXECUTOR runs the new agent              │
└─────────────────────────────────────────────────────────┘
```

### Components

#### 1. **Consultant Agent** 🤔
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

#### 2. **Architect Agent** 🏛️
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

#### 3. **Builder Agent** 👷
**Role:** Code Generation

- Receives approved JSON blueprint
- Generates **production-ready Python code** using Google ADK
- Enforces strict syntax and import rules
- Validates all agent definitions

**Enforces:**
- ✅ Only approved imports from Google ADK
- ✅ Proper agent configuration with model & tools
- ✅ Valid JSON blueprint structure
- ❌ No hardcoded secrets or API keys
- ❌ No deprecated packages

#### 4. **Storage Manager** 💾
**Role:** Persistent Storage

- Saves blueprints as JSON files
- Saves generated code as Python files
- Organizes agents by name in `agent_factory_storage/`

**Directory structure:**
```
agent_factory_storage/
├── personal_shopper/
│   ├── blueprint.json    # System design
│   └── agent.py          # Generated code
├── email_assistant/
│   ├── blueprint.json
│   └── agent.py
└── ...
```

#### 5. **Dynamic Executor** ⚡
**Role:** Runtime Execution

- Dynamically loads generated `.py` files using `importlib`
- Instantiates and runs agents without kernel restart
- Enables iterative development & testing

---

## 📊 Data Flow

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
   │  ├─ Design blueprint
   │  ├─ Show to user
   │  ├─ Get feedback
   │  └─ Refine or approve
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

## 🎮 Usage Examples

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
GOOGLE_API_KEY=your_api_key_here        # Required
GEMINI_MODEL=gemini-2.5-flash-lite      # Model to use

# Optional
FACTORY_STORAGE_PATH=agent_factory_storage  # Where to save agents
LOG_LEVEL=INFO                              # Logging level
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
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .env                              # Configuration (not in git)
│
├── src/
│   └── root.ipynb                    # Main Jupyter notebook
│       ├── Cell 1: Environment verification
│       ├── Cell 2: Architecture overview + diagrams
│       ├── Cell 3: Core setup & configuration
│       ├── Cell 4: Storage Manager
│       ├── Cell 5: Architect Agent
│       ├── Cell 6: Consultant Agent
│       ├── Cell 7: Builder Agent
│       ├── Cell 8: Orchestrator
│       ├── Cell 9: Dynamic Executor
│       └── Cell 10: Run Factory + Quick Reference
│
├── agent_factory_storage/             # Generated agents (created at runtime)
│   ├── personal_shopper/
│   │   ├── blueprint.json
│   │   └── agent.py
│   └── ...
│
├── info.md                           # Additional documentation
└── LICENSE                           # MIT License
```

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

## 📈 Future Enhancements

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

- [Google Agent Development Kit (ADK)](https://github.com/google/generative-ai-python)
- [Google Gemini API](https://ai.google.dev)
- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

---

## 📝 License

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