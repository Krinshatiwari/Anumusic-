# Powered By Team krishna_Bots
from Anu.core.bot import Anony
from Anu.core.dir import dirr
from Anu.core.git import git
from Anu.core.userbot import Userbot
from Anu.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
