SYSTEM_PROMPT = (
    "You are a patent-claims classifier. Decide if the claim describes GREEN technology. "
    "Use ONLY the claim text. Do not use CPC codes or any metadata."
)

USER_PROMPT = """Claim text:
{claim_text}

Task:
Return JSON with keys:
- llm_green_suggested: 0 or 1
- llm_confidence: low/medium/high
- llm_rationale: 1–3 sentences, cite phrases from the claim text
"""
