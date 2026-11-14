from google import genai
from config import(
    gemini_api_key,
    gemini_model,
)

client=genai.Client(
    api_key=gemini_api_key
)

def generate_response(prompt:str)-> str:
    response = client.models.generate_content(
        model=gemini_model,
        contents=prompt,
    )
    return response.text

    
print(generate_response("what is llm in 2 lines"))


