# Config time in minutes
config = {
    "focus": 25,
    "break": 5,
    "rest": 15
}

# convert to seconds
FOCUS_TIME = config["focus"] * 60
BREAK_TIME = config["break"] * 60
REST_TIME = config["rest"] * 60

MAX_SESSIONS = 7