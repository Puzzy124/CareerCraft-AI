# mentor_engine.py

def get_career_advice(domain, query):
    """
    Generate career advice for the given domain and user's question.
    Currently simulates a response. You can later integrate with AI/Gemini API.
    """

    # Load prompt template
    try:
        # Expect prompts/Data_Science.txt, prompts/Cloud_Engineering.txt, etc.
        prompt_file = f"prompts/{domain.lower().replace(' ', '_')}.txt"
        with open(prompt_file, "r") as f:
            base_prompt = f.read()
    except FileNotFoundError:
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
