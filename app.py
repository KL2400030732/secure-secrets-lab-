import os

api_key = os.getenv("API_KEY")

if api_key:
    print("API Key is configured successfully")
else:
    print("API Key is missing")