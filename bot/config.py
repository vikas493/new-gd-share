import os
import json
from distutils.util import strtobool as stb

# --------------------------------------
BOT_TOKEN = "5263755063:AAHHR4R5H2mG9yqkHLnmYvUd_r1apUa9-Cg"
GDRIVE_FOLDER_ID = "0AMXxDoHqOlqjUk9PVA"
# Default folder id.
OWNER_ID = 1487627714
# Example: OWNER_ID = 619418070
AUTHORISED_USERS = [1487627714, 1795525423, 685359441]
# Example: AUTHORISED_USERS = [63055333, 100483029, -1003943959]
INDEX_URL = "https://myindex.mahanbharat.workers.dev/1:"
IS_TEAM_DRIVE = True
USE_SERVICE_ACCOUNTS = False
# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))
