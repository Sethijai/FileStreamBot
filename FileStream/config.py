from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("29626867"))
    API_HASH = str(env.get("82b19751497d00e47c3032409d130423"))
    BOT_TOKEN = str(env.get("6404781810:AAHMvqRwt3PfTt2IkOocvg8-yQGxuPc7TKM"))
    OWNER_ID = int(env.get('OWNER_ID', '6650589235'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('mongodb+srv://namanjain123eudhc:opmaster@cluster0.5iokvxo.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://telegra.ph/file/a264bf1f2e134631f1dc8.jpg")
    START_PIC = env.get('START_PIC', "https://telegra.ph/file/5fa3f9f5fcd8240148eb0.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://telegra.ph/file/bd21f0b96f8af58016488.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("-1002138960289", None))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("-1002128449830", None))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



