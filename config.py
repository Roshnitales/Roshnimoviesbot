import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PRIVATE_GROUP_ID = os.getenv("PRIVATE_GROUP_ID")
PUBLIC_GROUP_ID = os.getenv("PUBLIC_GROUP_ID")
