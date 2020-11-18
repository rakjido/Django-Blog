from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

KEY_SET = "iHlsPAeadeMeFhv8T9ttE4uwsu3U5b3ava2fKmed4rDj9v9vBN"

DATABASE_SET = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG_SET = True


HOST_SET = ["*"]

CONFIG_EMAIL_USER = "youremail@mail.com"
CONFIG_EMAIL_PASSWORD = "password"