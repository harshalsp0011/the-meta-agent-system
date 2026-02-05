# Project Summary

## Project name and your role
The Meta Agent Factory System - AI/ML Engineer

## What the project does (business problem it solves)
This system converts a plain-language request into a working multi-agent solution. It reduces the time and expertise required to design agent architectures, write boilerplate, and iterate on requirements by automating strategy selection, blueprinting, and code generation with human approvals between phases.

## Tech stack used
Python, Streamlit, Google ADK, Google Gemini (google-genai), LangChain, LangGraph, Pydantic, SQLAlchemy (optional), dotenv, Jupyter Notebooks

## Main components/modules you built
- Consultant/Strategy step that turns a vague request into concrete architectural options.
- Architect step that produces a JSON blueprint and handles iterative user feedback until approval.
- Builder step that generates production-ready Python agent code from the approved blueprint.
- Dynamic execution layer that loads and runs the generated agent without restarting the runtime.
- Streamlit UI that guides users through each phase with clear state and review checkpoints.
- Model routing helper that selects and falls back across LLMs based on task type.

## Key technical details
### How data flows (input -> processing -> output)
User request -> Consultant proposes strategies with pros/cons -> User selects a strategy -> Architect generates JSON blueprint -> User approves or requests changes -> Builder generates Python code -> Dynamic loader imports and runs the agent -> Outputs are stored as JSON + Python files.

### Any special algorithms, LLM usage, validation logic
- Multi-agent workflow with human-in-the-loop checkpoints to prevent incorrect designs from moving forward.
- LLM-backed strategy generation, blueprint creation, and code synthesis, each scoped to a specific role.
- Model routing with fallback chains to balance cost, latency, and quality per task category.
- Blueprint-driven generation to enforce structure, reduce variability, and keep outputs consistent.

### Database schema design (SCD Type 2, star schema, etc.)
No fixed warehouse schema is required. The system persists artifacts as JSON blueprints and generated Python files; SQLAlchemy is included as an optional integration point for persistence if needed later.

## Collaboration/teamwork aspects
### Who you worked with (data engineers, business stakeholders, non-technical team)
The repository does not specify a team roster. Typical usage involves collaboration with product owners or domain experts who provide requirements and validate the design during approval steps.

### Tools used for planning (Jira, GitHub, Confluence)
Git is part of the workflow; the repo does not explicitly mention Jira or Confluence.

## Impact/results
Enables a structured, repeatable pipeline for generating agent systems and shortens iteration cycles through interactive approvals. No explicit performance or business metrics are documented in the repository.

## Any special features
- Human-in-the-loop approvals between strategy and blueprint phases.
- Dynamic execution without kernel restart for fast iteration.
- Secure configuration via environment variables for API keys and model selection.
- Streamlit UI for a guided, step-based user experience.
- Multi-model routing with fallback support to improve reliability.
