import os
from dotenv import load_dotenv

load_dotenv()


gemini_api_key=os.getenv('gemini_api_key')
gemini_model=os.getenv('gemini_model','gemini-3.5-flash')


if not gemini_api_key:
    raise RuntimeError(
        'gemini_api_key is not set, please add it .env file'
    )


