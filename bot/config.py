import os


class Config:
    PORT = os.environ.get("PORT", "8080")
    WEBHOOK = os.environ.get("WEBHOOK", "True")
    API_ID = os.environ.get("API_ID", "27194346")
    API_HASH = os.environ.get("API_HASH", "84f1c24b227fa7681565e98b51b9f2a3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6996037099:AAH-m90FBQyLxOwQarWpPM_GFmrUSw3LUn8")
    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002116542152")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Tokyo:Tokyo@cluster0.qtvp8pj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "6874351976 6047510747").split(" ")]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "https://screen-shot.koyeb.app")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
