import os

def get_available_domains():
    """
    Returns a list of available domain prompt files in the 'prompts' folder.
    Each filename is converted to a readable domain name.
    """
    if not os.path.exists("prompts"):
        return []
    return [
        filename.replace(".txt", "").replace("_", " ").title()
        for filename in os.listdir("prompts")
        if filename.endswith(".txt")
    ]

def load_prompt(domain):
    """
    Loads the domain-specific prompt file.
    If not found, returns a default prompt and a suggestion message.
    """
    prompt_file = f"prompts/{domain.lower().replace(' ', '_')}.txt"
    if os.path.exists(prompt_file):
        with open(prompt_file, "r") as f:
            return f.read(), None
    else:
        available = get_available_domains()
        suggestion = (
            f"⚠️ Domain '{domain}' not found.\n"
            f"Available domains: {', '.join(available) if available else 'None'}\n"
            f"Using default mentor prompt instead.\n"
        )
        return "You are a helpful career mentor.", suggestion

def build_full_prompt(base_prompt, query):
    """
    Combines the base prompt with the user's question.
    """
    return f"{base_prompt}\n\nUser Question: {query}"

def simulate_gemini_response(domain):
    """
    Simulates a Gemini response based on the domain.
    """
    return (
        f"[Simulated Gemini Response]\n"
        f"Based on your interest in {domain}, here's some advice:\n"
        f"- Focus on relevant skills for {domain}.\n"
        f"- Build projects and practice regularly.\n"
        f"- Network with professionals in this field."
    )

def get_career_advice(domain, query):
    """
    Main function to generate career advice.
    Loads the appropriate prompt and returns a simulated response.
    """
    base_prompt, suggestion = load_prompt(domain)
    if suggestion:
        print(suggestion)
    full_prompt = build_full_prompt(base_prompt, query)
    response = simulate_gemini_response(domain)
    return response

# Example usage
print(get_career_advice("data science", "How do I get started in this field?"))
``
