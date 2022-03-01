import os
from dotenv import load_dotenv 

load_dotenv()

# Canvas course ids to check
COURSES_IDS = [137548, 138042, 134687, 136065]

# The amount of days to be notified in advance
NOTIFY_DAY = 10

# Log errors
LOG_ERRORS = True

# Error log filename
ERROR_LOG_FILE = 'error.log'

# Canvas API Token
CANVAS_API_USER_TOKEN = os.getenv('CANVAS_API_USER_TOKEN')

# SMTP
SMTP_SERVER_NAME = 'smtp.gmail.com'
SMTP_PORT = '587'

# Receiver
SEND_TO_EMAIL = os.getenv('SEND_TO_EMAIL')

# Sender
SEND_FROM_EMAIL = os.getenv('SEND_FROM_EMAIL')
SEND_FROM_PASS = os.getenv('SEND_FROM_PASS')
