def generate_ad_prompt(product_name, target_audience, main_benefit):
    """
    Generates a highly optimized prompt for AI (Claude/ChatGPT) 
    to write Meta Ad copy based on digital marketing best practices.
    """
    prompt = f"""
    Act as an expert Conversion Copywriter and Digital Marketer. 
    Write 3 variations of a Meta (Facebook/Instagram) Ad for the following:
    
    - Product: {product_name}
    - Target Audience: {target_audience}
    - Main Benefit: {main_benefit}
    
    Ensure the copy follows the AIDA (Attention, Interest, Desire, Action) framework.
    Include a catchy headline, engaging primary text, and a strong Call-to-Action (CTA).
    Keep the tone persuasive but natural.
    """
    return prompt

# Example Usage
if __name__ == "__main__":
    print("--- Marketing AI: Meta Ad Prompt Generator ---")
    product = input("Enter Product Name: ")
    audience = input("Enter Target Audience: ")
    benefit = input("Enter Main Benefit: ")
    
    final_prompt = generate_ad_prompt(product, audience, benefit)
    
    print("\n✅ Copy and paste this prompt into Claude or ChatGPT:\n")
    print(final_prompt)
