# Streamlit UI Setup & Usage

## Installation

### 1. Install Streamlit
```bash
pip install streamlit
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
streamlit --version
```

---

## Running the UI

### Start the Application
```bash
streamlit run streamlit_ui.py
```

This will:
- Open a local web server (usually http://localhost:8501)
- Launch the Meta-Agent Factory UI in your browser
- Display the interactive agent generation interface

### Stop the Application
Press `Ctrl+C` in terminal

---

## How to Use

### Step 1: Describe Your Agent
- Enter a detailed description of what agent you need
- Example: "I need a customer support agent that can search our knowledge base and send emails"
- Click **"✨ Generate Strategies"**

### Step 2: Choose Strategy
- Review **Strategy A** (Rule-Based) vs **Strategy B** (ML-Based)
- Compare pros/cons, time, and cost estimates
- Click **"Select"** on your preferred strategy

### Step 3: Review Blueprint
- See the system design and components
- Review required tools
- Either:
  - Click **"✅ Approve"** to proceed to code generation
  - Click **"✏️ Request Changes"** to revise
  - Click **"↩️ Back"** to choose different strategy

### Step 4: Get Your Code
- View the generated Python agent code
- Options:
  - **📥 Download Code** - Save as `agent.py`
  - **📋 Copy** - Copy to clipboard
  - **▶️ Run Test** - Test the agent
  - **🔄 Regenerate** - Create alternative version

---

## Features

### Interactive Workflow
✅ 4-step process with visual feedback
✅ Side-by-side strategy comparison
✅ Blueprint approval/revision
✅ Code download and testing

### Sidebar Information
- Current step progress
- Agent statistics
- Model and temperature settings
- Quick links and resources

### State Management
- Tracks entire workflow
- Saves user inputs
- Maintains agent history
- Allows backtracking

---

## Integration with LangChain

Currently, the UI uses **simulated responses**. To connect to your actual LangChain agents:

### Update Step 2 (Strategy Generation)
Replace this section in `streamlit_ui.py`:
```python
# Change from simulation:
st.session_state.strategies = {...}

# To actual call:
from src.root_LangChain_version import consultant_agent
st.session_state.strategies = consultant_agent(user_request)
```

### Update Step 3 (Blueprint Design)
Replace:
```python
# From simulation:
st.session_state.blueprint = {...}

# To actual call:
from src.root_LangChain_version import architect_agent
st.session_state.blueprint = architect_agent(selected_strategy)
```

### Update Step 4 (Code Generation)
Replace:
```python
# From simulation:
st.session_state.generated_code = '''...'''

# To actual call:
from src.root_LangChain_version import builder_agent
st.session_state.generated_code = builder_agent(blueprint)
```

---

## Customization

### Change App Title
Edit line in `streamlit_ui.py`:
```python
st.markdown("# My Custom Title")
```

### Modify Colors/Styling
Edit the CSS section:
```python
st.markdown("""
<style>
    # Your custom CSS here
</style>
""", unsafe_allow_html=True)
```

### Add Custom Tools
In Step 3, add:
```python
tools_list = ["tool1", "tool2", "tool3"]
selected_tools = st.multiselect("Select Tools", tools_list)
```

---

## Troubleshooting

### "Module not found" error
```bash
pip install streamlit langchain langchain-openai python-dotenv
```

### API Key issues
1. Check `.env` file has `OPENAI_API_KEY`
2. Run: `streamlit run streamlit_ui.py`
3. Check sidebar for API key status

### Port already in use
Use different port:
```bash
streamlit run streamlit_ui.py --server.port 8502
```

### Session state not persisting
Streamlit clears state on code changes. This is normal.
- Full page refresh clears it
- Code changes trigger reset

---

## Deployment

### Local Development
```bash
streamlit run streamlit_ui.py
```

### Deploy to Streamlit Cloud
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy from GitHub repo

### Docker Deployment
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "streamlit_ui.py", "--server.port=8501"]
```

Run with:
```bash
docker build -t meta-agent-factory .
docker run -p 8501:8501 meta-agent-factory
```

---

## Next: Connect to Real Agents

The UI is ready! Now connect it to your actual LangChain agents:

1. **Extract agent logic** from notebook
2. **Create Python module** with functions
3. **Import in streamlit_ui.py**
4. **Replace simulated data** with real calls

Example structure:
```
src/
  ├── root_LangChain_version.ipynb
  ├── agents.py (new - extract agent logic)
  └── tools.py (new - tool registry)

streamlit_ui.py (updated - use real agents)
```

Ready to customize?
