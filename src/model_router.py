"""Lightweight model routing helper.

Maps task types to preferred models so you can minimize cost and maximize quality:
- Sonar:            orchestration / glue / handoffs (fast, cheap)
- Sonar Reasoning:  architecture / complex reasoning
- Claude 3.5 Sonnet:heavy code generation / debugging / implementation

Usage:
    from src.model_router import pick_model
    model = pick_model("architecture design")
    # -> "sonar-reasoning"

    # Integrate with your LLM client of choice (OpenAI/Anthropic/etc.).
"""

from __future__ import annotations
from typing import Dict, Callable, List

# Keyword-based routing table
# Base model choices per task keyword
MODEL_MAP: Dict[str, str] = {
    # Orchestration / glue
    "orchestration": "sonar",
    "handoff": "sonar",
    "routing": "sonar",
    "chat": "sonar",
    "summary": "sonar",

    # Reasoning / architecture
    "architecture": "sonar-reasoning",
    "design": "sonar-reasoning",
    "reasoning": "sonar-reasoning",
    "blueprint": "sonar-reasoning",
    "plan": "sonar-reasoning",

    # Code / debug / implement
    "code": "claude-3.5-sonnet",
    "implement": "claude-3.5-sonnet",
    "debug": "claude-3.5-sonnet",
    "fix": "claude-3.5-sonnet",
    "refactor": "claude-3.5-sonnet",
}

DEFAULT_MODEL = "sonar"  # safe, fast, cheap fallback

# Priority chains (primary → fallbacks) per task family
# Adjust model names to your actual provider IDs.
MODEL_PRIORITIES: Dict[str, List[str]] = {
    "orchestration": ["google-fast", "sonar", "sonar-reasoning"],
    "reasoning": ["google-pro-reasoning", "sonar-reasoning", "sonar"],
    "code": ["google-code", "claude-3.5-sonnet", "sonar-reasoning"],
}

# Optional: alternate keys you can reference for fallbacks (e.g., two Perplexity keys)
ALTERNATE_MODEL_ALIASES: Dict[str, List[str]] = {
    "sonar": ["sonar-alt-1", "sonar-alt-2"],  # e.g., multiple Perplexity keys
    "sonar-reasoning": ["sonar-reasoning-alt"],
    "google-fast": ["google-fast-alt"],
    "google-pro-reasoning": ["google-pro-reasoning-alt"],
    "google-code": ["google-code-alt"],
}


def pick_model(task_type: str) -> str:
    """Choose a model based on task keywords.

    Args:
        task_type: short description of the task, e.g. "architecture design" or "code generation".

    Returns:
        Model name string.
    """
    lowered = task_type.lower()
    for keyword, model in MODEL_MAP.items():
        if keyword in lowered:
            return model
    return DEFAULT_MODEL


def model_fallback_chain(task_type: str) -> List[str]:
    """Return a priority-ordered list of model ids for this task."""
    primary = pick_model(task_type)

    # Pick a priority family if available; else fall back to just the primary
    if "orchestration" in task_type.lower():
        chain = MODEL_PRIORITIES.get("orchestration", [primary])
    elif any(k in task_type.lower() for k in ["design", "architecture", "reasoning", "plan", "blueprint"]):
        chain = MODEL_PRIORITIES.get("reasoning", [primary])
    elif any(k in task_type.lower() for k in ["code", "implement", "debug", "fix", "refactor"]):
        chain = MODEL_PRIORITIES.get("code", [primary])
    else:
        chain = [primary]

    # Expand aliases for each entry to support multiple API keys/providers
    expanded: List[str] = []
    for model in chain:
        expanded.append(model)
        expanded.extend(ALTERNATE_MODEL_ALIASES.get(model, []))

    # Deduplicate while preserving order
    seen = set()
    ordered = []
    for m in expanded:
        if m not in seen:
            seen.add(m)
            ordered.append(m)
    return ordered


def get_llm_with_fallback(
    task_type: str,
    client_factory: Callable[[str], object],
) -> object:
    """
    Instantiate an LLM client with fallback across multiple providers/models.

    Args:
        task_type: short description ("orchestration", "architecture design", "code generation", etc.)
        client_factory: function that takes model_name -> returns initialized client.
                       It should raise on auth/credit errors so we can try next.

    Returns:
        An initialized LLM client.

    Raises:
        RuntimeError if all candidates fail.
    """
    errors = []
    for model_name in model_fallback_chain(task_type):
        try:
            return client_factory(model_name)
        except Exception as exc:  # Broad by design to catch auth/credit failures
            errors.append(f"{model_name}: {exc}")
            continue
    raise RuntimeError(f"All model fallbacks failed for task '{task_type}'. Errors: {errors}")


# OPTIONAL: Example integration stub (replace with your actual client calls)
#
# from langchain_openai import ChatOpenAI
# from anthropic import Anthropic
#
# def client_factory(model_name: str):
#     if model_name.startswith("claude"):
#         return Anthropic(api_key=..., model=model_name)  # replace with real init
#     if model_name.startswith("google"):
#         # Replace with your Google ADK/Gemini client
#         return ChatOpenAI(model=model_name, temperature=0)  # placeholder if OpenAI-compatible
#     else:
#         # Sonar / Sonar-Reasoning via OpenAI-compatible endpoint (Perplexity, etc.)
#         return ChatOpenAI(model=model_name, temperature=0)
#
# def get_llm(task_type: str):
#     return get_llm_with_fallback(task_type, client_factory)
