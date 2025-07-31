from model.screen import Screen
from controller.controller import Controller
import sqlite3
import json
from pathlib import Path

def load_config():
    """
    Loads config from the /config/settings.json file.
    """
    settings_path = Path(__file__).parent / "config" / "settings.json"
    with open(settings_path, "r") as f:
        return json.load(f)

def main():
    """
    The main application loop.
    """
    config = load_config()
    db_path = config["db_path"]

    controller = Controller(db_path)
    screens = Screen.read_all(controller.connection)


if __name__ == "__main__":
    main()