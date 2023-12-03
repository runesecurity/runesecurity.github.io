from datetime import datetime

AUTHOR = '@rune_sec'
SITENAME = 'runesec | CTI Research + Blog'
SITEURL = "https://runesecurity.github.io"

THEME = "themes/Flex"
PATH = "content"
OUTPUT_PATH = 'output'

USE_SHORTCUT_ICONS = True
FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/profile.png'
DISABLE_URL_HASH = True

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

COPYRIGHT_YEAR = datetime.now().year

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("cti Researcher | runesec", "#"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/rune_sec"),
    ("github", "https://github.com/runesecurity")
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True