"""Generate a pristine template SQLite database (template.db) containing the
schema required by Screen Locator. Run from project root:
    python packaging/build_template_db.py
This will (re)create packaging/template.db.
"""
from pathlib import Path
import sqlite3

pkg_dir = Path(__file__).parent
db_path = pkg_dir / "template.db"
if db_path.exists():
    db_path.unlink()
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.executescript("""
CREATE TABLE "Locations" (
	"LocationID"	INTEGER,
	"Description"	TEXT,
	PRIMARY KEY("LocationID" AUTOINCREMENT)
);
CREATE TABLE "Screens" (
	"ScreenID"	INTEGER,
	"LocationID"	INTEGER NOT NULL,
	"Quantity"	INTEGER,
	"Design"	TEXT,
	"CustomerName"	TEXT,
	"Description"	TEXT,
	"InUse"	INTEGER,
	PRIMARY KEY("ScreenID" AUTOINCREMENT)
);
""")
conn.commit(); conn.close()