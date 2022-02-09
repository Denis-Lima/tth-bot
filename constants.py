import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass
TOKEN = os.environ.get('TOKEN')
