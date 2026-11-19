import os
from dotenv import load_dotenv

load_dotenv()

ELASTIC_ENDPOINT = os.getenv('ELASTIC_ENDPOINT')
ELASTIC_API_KEY = os.getenv('ELASTIC_API_KEY')
APIS_API_KEY = os.getenv('APIS_API_KEY')

#  MariDB 접속 정보

DATABASE_URL = os.getenv("DATABASE_URL")
SESSION_SECRET_KEY = os.getenv("SESSION_SECRET_KEY")

# gpt 키
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')