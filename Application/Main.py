from controller.controller import Controller
from view.main_view import MainView
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import json

def _ensure_valid_db(config_path: Path) -> bool:
    """
    Ensure settings.json points to an existing sqlite db, otherwise prompt user.
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    db_path = config.get('db_path', '')
    changed=False
    if not db_path or not Path(db_path).is_file():
        # ask user using temporary hidden root then destroy it to avoid duplicate Tk roots
        temp_root = tk.Tk(); temp_root.withdraw()
        messagebox.showwarning('Database Missing', 'Database path is not set or file not found. Please select a database file.', parent=temp_root)
        new_path = filedialog.askopenfilename(title='Select SQLite DB', parent=temp_root, filetypes=[('SQLite DB','*.db'),('All','*.*')])
        if not new_path:
            messagebox.showerror('No Database Selected', 'Application cannot start without a database. Exiting.', parent=temp_root)
            temp_root.destroy()
            sys.exit(1)

        # update the settings.json file in config/
        config['db_path'] = new_path
        changed=True
        with open(config_path,'w') as f:
            json.dump(config, f, indent=2)
        messagebox.showinfo('Database Set', f'Database path updated to:\n{new_path}', parent=temp_root)
        temp_root.destroy()
        return changed

    return changed

def main():
    """
    The main application loop.
    """
    # determine base directory (support PyInstaller frozen exe)
    if getattr(sys, 'frozen', False):
        base_dir = Path(sys.executable).parent
    else:
        base_dir = Path(__file__).parent
    config_dir = base_dir / 'config'
    config_dir.mkdir(parents=True, exist_ok=True)
    config_path = config_dir / 'settings.json'
    # create empty settings file if missing so _ensure_valid_db can open it safely
    if not config_path.exists():
        config_path.write_text('{}')
    prompted = _ensure_valid_db(config_path)
    controller = Controller()
    main_view = MainView(controller)
    if prompted:
        # bring window to front and focus
        main_view.after(100, lambda: (main_view.lift(), main_view.focus_force()))
    main_view.mainloop()

if __name__ == "__main__":
    main()