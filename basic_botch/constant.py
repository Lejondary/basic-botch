import os
from dotenv import load_dotenv

load_dotenv('.env')

#config = {
#   **dotenv_values(".env.shared"),  # load shared development variables
#    **dotenv_values(".env.secret"),  # load sensitive variables
#    **os.environ,  # override loaded values with environment variables
#}

TOKEN = os.getenv('BOT_TOKEN')
OWNER = os.getenv('OWNER')
PREFIX = os.getenv('PREFIX')
