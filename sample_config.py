class Config(object):
    
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("6043283784:AAHLV11M9g3gaDj5dE-Sr5fKhSCd8CT-lOc")
    # The Telegram API things
    APP_ID = int(os.environ.get("7143337")
    API_HASH = os.environ.get("1afa55a5f3bf7058c843d1b290f79c49")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("1284818583").split())
    DOWNLOAD_LOCATION = os.path.isdir("./DOWNLOADS") 
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 1
    # watermark file
    DEF_WATER_MARK_FILE = ""
