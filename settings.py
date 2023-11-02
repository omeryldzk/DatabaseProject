DEBUG = False
PORT = 8090
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True

PASSWORDS = {
    "admin": "$pbkdf2-sha256$29000$PIdwDqH03hvjXAuhlLL2Pg$B1K8TX6Efq3GzvKlxDKIk4T7yJzIIzsuSegjZ6hAKLk",
    "normaluser": "abcd123",
}

ADMIN_USERS = ["admin"]