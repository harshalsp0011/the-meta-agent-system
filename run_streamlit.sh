#!/bin/bash
# Meta-Agent Factory - Streamlit UI Launcher
# Quick start script to run the Streamlit UI

echo "🤖 Meta-Agent Factory - Streamlit UI"
echo "════════════════════════════════════"
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null
then
    echo "❌ Streamlit not installed"
    echo "Installing Streamlit..."
    pip install streamlit langchain langchain-openai python-dotenv
    echo ""
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found"
    echo "Please create .env with OPENAI_API_KEY"
    exit 1
fi

# Check if API key is set
if ! grep -q "OPENAI_API_KEY=" .env; then
    echo "❌ OPENAI_API_KEY not found in .env"
    exit 1
fi

echo "✅ All checks passed"
echo ""
echo "🚀 Starting Streamlit UI..."
echo "   Open browser: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop"
echo ""

streamlit run streamlit_ui.py
