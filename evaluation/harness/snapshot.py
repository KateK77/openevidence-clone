"""Read-only oracle. Deliberately excludes users, password hashes and sessions."""
import sqlite3, json, sys
from pathlib import Path
db=sqlite3.connect(Path(sys.argv[1]).resolve().as_uri()+'?mode=ro',uri=True)
db.row_factory=sqlite3.Row
tables=('evidence_preferences','evidence_conversation','evidence_turn','evidence_evidence','evidence_publication','evidence_savedpublication','evidence_savedsearch')
print(json.dumps({table:[dict(row) for row in db.execute('SELECT * FROM '+table)] for table in tables},ensure_ascii=True))
