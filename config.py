from os import environ

#TG Credentials
API_ID = int(environ.get('API_ID', '29081699'))
API_HASH = environ.get('API_HASH', '4c4beb5bf57a6d52a4cda249a98f0980')
BOT_TOKEN = environ.get('BOT_TOKEN', '6233366267:AAF9Jxt2eAU6CBnk4Zp1mlk7kxSOc8o2ics')

#Website Credentials
API_KEY = environ.get('API_KEY', 'd0ac58b10c9edfe7e79c8df7aaf79dcb2b7928af')
API_URL = environ.get('API_URL', 'https://url.staus.in/api')
WEB_NAME = environ.get('WEB_NAME', 'urlstaus')

#Optional
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', 'https://t.me/pandaztalks')
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', 'https://t.me/pandaznetwork')
