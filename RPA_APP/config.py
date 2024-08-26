"""DEFAULT VARIABLES"""
from robocorp import vault, storage


secrets = vault.get_secret("Aljazeera")
locators = storage.get_json("Aljazeera's News Extraction")


# >>>>>>>>>EMAIL CONFIGS>>>>>>>>>
# SMTP_HOST = "smtp.gmail.com"
SMTP_HOST = secrets["SMTP_HOST"]
# SMTP_PORT = 587
SMTP_PORT = secrets["SMTP_PORT"]
# SMTP_USER = "rickpincelli@gmail.com"
SMTP_USER = secrets["SMTP_USER"]
# SMTP_PASWORD = "aqjl azga tfeq wszb"
SMTP_PASWORD = secrets["SMTP_PASWORD"]
# <<<<<<<<<EMAIL CONFIGS<<<<<<<<<

# >>>>>>>>>ALJAZEERA'S RPA CONFIGS>>>>>>>>>
EMAIL_ALJAZEERA = locators["email_aljazeera"]
SERCH_PHRASE_ALJAZEERA = locators["search_phrase_aljazeera"]
SHOW_MORE_ALJAZEERA = locators["show_more_aljazeera"]
# <<<<<<<<<ALJAZEERA'S RPA CONFIGS<<<<<<<<<
