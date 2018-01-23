from os import environ

try:
    import env as _env
    env = "dev"
except Exception as e:
    env = "prod"

_SETTINGS = {}

if env == "dev":
    _SETTINGS = {
        "SID": _env.SID,
        "token": _env.token,
        "to_number": _env.to_number,
        "from_number": _env.from_number,
        "email": _env.email,
        "password": _env.password
    }
else:
    _SETTINGS = {
        "SID": environ.get('SID'),
        "token": environ.get('token'),
        "to_number": environ.get('to_number'),
        "from_number": environ.get('from_number'),
        "email": environ.get('email'),
        "password": environ.get('password')
    }
