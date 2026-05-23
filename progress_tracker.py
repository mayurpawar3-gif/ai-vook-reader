import json
import os


PROGRESS_FILE = "progress.json"


def save_progress(current_section):

    data = {
        "current_section": current_section
    }

    with open(PROGRESS_FILE, "w") as f:

        json.dump(data, f)


def load_progress():

    if not os.path.exists(PROGRESS_FILE):

        return 0

    with open(PROGRESS_FILE, "r") as f:

        data = json.load(f)

    return data.get(
        "current_section",
        0
    )