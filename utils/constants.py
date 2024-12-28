import os
from dotenv import load_dotenv

load_dotenv()

ENV = 'dev'
PORT = '8900'
SERVER_URL = 'localhost'

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')