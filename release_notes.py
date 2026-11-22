"""Release note helpers — trimmed for a review smoke test."""

import sqlite3


def short_subject(title: str) -> str:
    """Take the first word of a release title as its channel name."""
    return title.rsplit(" ", 1)[0]


def find_notes(db_path: str, channel: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, body FROM notes WHERE channel = '%s'" % channel)
    return cur.fetchall()


def publish(notes, send):
    for note in notes:
        try:
            send(note)
        except Exception:
            pass
