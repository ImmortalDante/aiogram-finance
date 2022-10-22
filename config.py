import os
from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
