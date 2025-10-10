
def get_career_advice(domain, query):
    # Load prompt template
    try:
        with open(f"prompts/{domain.lower().replace(' ', '_')}.txt", "r") as f:
            base_prompt = f.read()
    except FileNotFoundError:
        base_prompt = "You are a helpful career mentor."

    # Combine prompt and query
    full_prompt = f"{base_prompt}

User Question: {query}"

    # Simulate Gemini response (replace with actual API call)
    response = f"[Gemini Response]
Based on your interest in {domain}, here's some advice: ..."
    return response
