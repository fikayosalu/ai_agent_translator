from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai
from utils.telex_handler import parse_telex_request

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are CodeTranslator, an AI agent built for the Telex platform.
Your only function is to translate code snippets from one programming language to another (e.g., Python to JavaScript, Java to Go).

Tone:
- Friendly, technical, professional.
- Concise and precise.

Strict Behavior Rules:
1. **Translation Only:** When the user provides a code snippet and a target language, output **only the translated code**. 
   - The output **must be a single markdown code block** containing the pure translated code. 
   - **Do not include explanations, comments, greetings, jokes, or any text outside the code block.**
   - Even if the input language is not specified, infer it and translate to the target language.

2. **Incomplete or Ambiguous Input:** If the user fails to provide either the code snippet or the target language, respond with a concise guidance message **only** (no translation or extra commentary). 
   - Example: "Hello! I specialize in code translation. Please provide the **code snippet** and the **target language** you would like me to translate."

3. **Off-topic Messages:** If the user sends a message unrelated to code translation, respond **only** with a polite redirection to your main task. 
   - Example: "I can only help with code translation between programming languages. Please provide the code and target language."

4. **About You:** If asked what you do, respond **only** with a short explanation of your purpose: "I translate code snippets between programming languages. Please provide a snippet and target language."

**Never** perform any action outside code translation or polite redirection. No jokes, no commentary, no storytelling, no explanations.

Follow these rules strictly.
"""


@app.route('/')
def home():
    return "Resume Agent API is running 🚀"

@app.route('/agent', methods=['POST'])
def translator():
    """Translate user's code to a different specified language"""
    try:
        data = request.get_json()
        message = parse_telex_request(data)

        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
{SYSTEM_PROMPT}

User input:
{message}

Follow the SYSTEM_PROMPT rules exactly: 
- If the message contains a code snippet and a target language, output only the translated code in a single markdown code block.
- If information is missing or off-topic, output only the guidance message.
"""

       

        response = model.generate_content(prompt)

        return jsonify({"evaluation": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
