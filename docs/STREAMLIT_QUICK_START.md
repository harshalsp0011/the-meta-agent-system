# Streamlit UI - Quick Start Guide

## What You Now Have

A professional **web-based UI** for the Meta-Agent Factory system:

```
📄 streamlit_ui.py (553 lines)
   └─ Complete Streamlit application with 4-step workflow

📄 STREAMLIT_SETUP.md (231 lines)
   └─ Detailed setup and integration guide

📄 run_streamlit.sh (39 lines)
   └─ Quick start launcher script
```

---

## Get Started in 2 Minutes

### Option 1: Run Script (Easiest)
```bash
chmod +x run_streamlit.sh
./run_streamlit.sh
```

### Option 2: Direct Command
```bash
pip install streamlit langchain langchain-openai python-dotenv
streamlit run streamlit_ui.py
```

### Open in Browser
```
http://localhost:8501
```

---

## What the UI Does

### 4-Step Interactive Workflow

**Step 1: Describe Agent**
- Type what kind of agent you need
- Click "Generate Strategies"

**Step 2: Choose Strategy**
- See Rule-Based vs ML-Based options
- Compare pros/cons and costs
- Select your preferred approach

**Step 3: Review Blueprint**
- See system design and components
- Approve or request changes
- Back up if needed

**Step 4: Get Code**
- Download working Python agent code
- Copy to clipboard
- Test it out
- Regenerate if needed

---

## Features Included

✅ **4-Step Wizard** - Clear workflow
✅ **Side-by-Side Comparison** - Compare strategies easily
✅ **Blueprint Visualization** - See system design
✅ **Code Download** - Get working code
✅ **Settings Sidebar** - Customize LLM model/temperature
✅ **State Management** - Track entire workflow
✅ **Responsive Design** - Works on all screen sizes
✅ **Professional Styling** - Nice gradients and colors

---

## Next: Connect to Real Agents

Currently uses simulated data. To connect to your actual LangChain agents:

### 1. Extract Agent Logic
Move agent functions from notebook to Python module:

```python
# agents.py
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor

def consultant_agent(request: str):
    """Generate 2 strategy options"""
    # Your consultant agent code
    return strategies

def architect_agent(strategy: str):
    """Design blueprint"""
    # Your architect agent code
    return blueprint

def builder_agent(blueprint: dict):
    """Generate code"""
    # Your builder agent code
    return code
```

### 2. Update streamlit_ui.py

Find these sections and replace:

**Around line 150** (Strategy generation):
```python
# OLD:
st.session_state.strategies = {...}

# NEW:
from agents import consultant_agent
st.session_state.strategies = consultant_agent(user_request)
```

**Around line 240** (Blueprint design):
```python
# OLD:
st.session_state.blueprint = {...}

# NEW:
from agents import architect_agent
st.session_state.blueprint = architect_agent(strategy)
```

**Around line 330** (Code generation):
```python
# OLD:
st.session_state.generated_code = '''...'''

# NEW:
from agents import builder_agent
st.session_state.generated_code = builder_agent(blueprint)
```

### 3. Test Integration
```bash
streamlit run streamlit_ui.py
```

---

## File Structure

```
project/
├── src/
│   ├── root_LangChain_version.ipynb (your agents)
│   └── agents.py (EXTRACT to here)
│
├── streamlit_ui.py ⭐ (the UI)
├── STREAMLIT_SETUP.md (documentation)
├── run_streamlit.sh (launcher)
│
├── MCP_INTEGRATION.md (what we built)
├── requirements.txt (dependencies)
└── .env (API keys)
```

---

## Development Flow

### For Testing (Simulated Mode)
```bash
streamlit run streamlit_ui.py
# Try the workflow with mock data
# See what it will look like
```

### For Integration (Real Mode)
1. Create `src/agents.py` with real agent functions
2. Update imports in `streamlit_ui.py`
3. Test with real OpenAI API calls
4. Deploy when ready

---

## Customization Ideas

### Add More Tools
```python
# In Step 3, add tool selector:
tools = st.multiselect("Select Tools", [
    "Knowledge Base",
    "Email",
    "Slack",
    "Database",
    "Web Search"
])
```

### Add Agent Testing
```python
# In Step 4, add test section:
if st.button("Test Agent"):
    test_input = st.text_input("Test message:")
    result = run_agent(generated_code, test_input)
    st.success(f"Result: {result}")
```

### Save Agent History
```python
# Track generated agents:
st.session_state.history.append({
    "timestamp": datetime.now(),
    "request": user_request,
    "strategy": selected_strategy,
    "code": generated_code
})
```

### Add Analytics
```python
# Track usage:
st.metric("Total Agents Generated", len(history))
st.metric("Most Popular Strategy", "ML-Based")
st.metric("Avg Generation Time", "2.5 mins")
```

---

## Troubleshooting

**Q: Port 8501 already in use**
```bash
streamlit run streamlit_ui.py --server.port 8502
```

**Q: API Key error**
- Check `.env` file exists
- Verify `OPENAI_API_KEY=your_key` is set
- Restart Streamlit after updating `.env`

**Q: Streamlit not found**
```bash
pip install streamlit
```

**Q: Session state not working**
- Page refresh clears state (normal)
- Code changes reset state (normal)
- Try: Don't use ctrl+C and restart

---

## What You Can Do Now

✅ **Run the UI** - `streamlit run streamlit_ui.py`
✅ **See the workflow** - 4-step interactive process
✅ **Test the UX** - Mock data flows through all steps
✅ **Download code** - See what users will get
✅ **Customize styling** - Edit CSS for your brand

---

## Next Steps

1. **Today**: Run the UI, see how it looks
2. **Tomorrow**: Extract agent logic from notebook
3. **Soon**: Connect real agents to UI
4. **Later**: Deploy to production (Streamlit Cloud or Docker)

---

**Your Streamlit UI is ready to use. Start with:**
```bash
streamlit run streamlit_ui.py
```

Then visit: http://localhost:8501
