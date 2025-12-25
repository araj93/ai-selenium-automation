import os
from dotenv import load_dotenv

load_dotenv()

USE_MOCK_AI = True  # 🔥 Set False when billing is enabled

def ask_ai(prompt: str) -> str:
    if USE_MOCK_AI:
        print("🧪 MOCK AI MODE ENABLED")
        print(f"Prompt sent to AI:\n{prompt[:200]}...\n")
        return "//input | //button | //a"  # safe generic XPath fallback

    # ===== REAL AI MODE (enable later) =====
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"⚠️ AI ERROR: {e}")
        return "//input | //button | //a"
