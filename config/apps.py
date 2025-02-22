# Application definition

NINJA_APPS = [
    "ninja_extra",
    "ninja_jwt",
]

API_APPS = [
    "ansc_auth",
]

INSTALLED_APPS = (
    [
        "admin_interface",
        "colorfield",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    + NINJA_APPS
    + API_APPS
)

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
