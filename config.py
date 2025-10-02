import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USER = os.environ.get('8456187383', '').split(',')
    AUTH_USERS = [int(8456187383) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "Crystal™"#Here You Can Change with Your Name  or any custom name or title you prefer
