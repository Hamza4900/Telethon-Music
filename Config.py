import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6508386922:AAFLNzk3fMLRIUjcFGXtewk8QEJ9o0KSBfM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgFjGt4AAzWubewyrf2i82Z-y92Kcr5bIxRf7J6BkyvlQB2qG0Rbg9XHQhJo48aLSKmjSsZaHUNZNSKLs-hwDSweyz992hqt0ou-_6JHj57c2ENBxcFZvbu0cL7jHntLkRpy16WVffBDUuLZUtQELuYeo8YEJcjlf1Z4BKFlWVVAIJJELcIp0XFTnLqyCHpEfeCEKIFOyOV-FULnz9B8M6oD7qJsdRgdfg3ylPttn6zFTlgfY8YzG7sZQXZxLLfkXV6NkVbz8EcnCyWiWq4kdg4eDFkvGAyuHqjzsOKmGCqTpDQg6-mTzgdz82FSP_A4dtaObMHNRWfLtADJzgqFoDGaU4DNIwAAAAHDjDalAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Konusanlarmusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "7575713445")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
