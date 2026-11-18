import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://test004.local")
API_USER = os.getenv("API_USER", "test_user")
API_PASS = os.getenv("API_PASS", "test_password")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))