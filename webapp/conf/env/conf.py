CONFIG = {
    "DJANGO_LOG_LEVEL": "INFO",
    "DATABASE": {
        "HOST": "localhost",
        "USERNAME": "root",
        "PASSWORD": "",
        "DB_NAME": "bagon",
        "PORT": "3306",
    },
    "DEBUG": False,
    "ALLOWED_HOSTS": ["*"],
}

EXTERNAL_SERVICES = {
    "GOOGLE": {
        "HOST": "XXX",
        "HEADERS": {
            "Content-Type": "application/json"
        },
        "KEY": "XXX",
    },
}
