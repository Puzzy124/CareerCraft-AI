# mentor_engine.py

import os

def get_available_domains():
    """Returns a list of available domain prompt files in the 'prompts' folder."""
    if not os.path.exists("prompts"):
        return []
    return [
        filename.replace(".txt", "").replace("_", " ").title()
        for filename in os.listdir("prompts")
        if filename.endswith(".txt")
    ]

def get_career_advice(domain, query):
    """
    Generate career advice for the given domain and user's question.
    Loads a domain-specific prompt if available, otherwise suggests alternatives.
    """

    # Normalize domain name to match file naming convention
    prompt_file = f"prompts/{domain.lower().replace(' ', '_')}.txt"

    # Try loading the domain-specific prompt
    try:
        with open(prompt_file, "r") as f:
            base_prompt = f.read()
    except FileNotFoundError:
        available = get_available_domains()
        suggestion = (
            f"⚠️ Domain '{domain}' not found.\n"
            f"Available domains: {', '.join(available) if available else 'None'}\n"
            f"Using default mentor prompt instead.\n"
        )
        print(suggestion)
        base_prompt = "You are a helpful career mentor."

    # Combine the base prompt with user query
    full_prompt = f"""{base_prompt}

User Question: {query}
"""

    # Simulate Gemini response (replace with actual API call later)
    response = (
        f"[Simulated Gemini Response]\n"
        f"Based on your interest in {domain}, here's some advice:\n"
        f"- Focus on relevant skills for {domain}.\n"
        f"- Build projects and practice regularly.\n"
        f"- Network with professionals in this field."
    )

    return response
