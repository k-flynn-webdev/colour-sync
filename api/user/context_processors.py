import os
from pathlib import Path
from dotenv import load_dotenv
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PARENT_DIR = Path(__file__).resolve().parent.parent.parent

"""
Expose Vars for `User` templates here
"""
def template_vars(request):
    load_dotenv(os.path.join(PARENT_DIR, '.env'))
    data = {}
    data['APP_NAME_FULL'] = os.getenv("APP_NAME_FULL", 'APP_NAME_FULL')
    data['APP_NAME_SHORT'] = os.getenv("APP_NAME_SHORT", 'APP_NAME_SHORT')
    data['META_AUTHOR'] = os.getenv("META_AUTHOR", 'META_AUTHOR')
    data['META_DESCRIPTION'] = os.getenv("META_DESCRIPTION", 'META_DESCRIPTION')
    data['SETTING_TYPE'] = os.environ['DJANGO_SETTINGS_MODULE']
    data['ACCOUNT_SESSION_REMEMBER'] = getattr(settings, "ACCOUNT_SESSION_REMEMBER", None)
    return data
