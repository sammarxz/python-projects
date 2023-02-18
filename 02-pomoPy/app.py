import time
import sys

from messages import title, welcome_input
from config import FOCUS_TIME, BREAK_TIME, REST_TIME, MAX_SESSIONS
from clear import clear
from notification import show_notification


def show_session(count):
    TIMER = [
        {
            "title": "Focus Time!",
            "time": FOCUS_TIME
        },
        {
            "title": "Take a Break!",
            "time": BREAK_TIME
        },
        {
            "title": "Rest Time!",
            "time": REST_TIME
        },
    ]
    actual_session = TIMER[-1] if count == MAX_SESSIONS else TIMER[count % 2]
    actual_session_title = actual_session["title"]

    print(actual_session_title, end="\n")
    show_notification(actual_session_title)

    while actual_session["time"]:
        session_minutes, session_seconds = divmod(actual_session["time"], 60)
        print("{:02d}:{:02d}".format(session_minutes, session_seconds), end="\r")
        time.sleep(1)
        actual_session["time"]-= 1

def start():
    count = 0
    task_title = input("Give your section a name: ")

    while count <= MAX_SESSIONS:
        clear()
        print(task_title)
        print("-----------------------")
        show_session(count)
        count+= 1

if __name__ == "__main__":
    try:
        while True:
            clear()
            print(title)
            answer = input(welcome_input)
            
            if str.lower(answer) == "q":
                break
            else:
                start()
    except KeyboardInterrupt:
        sys.exit(0)