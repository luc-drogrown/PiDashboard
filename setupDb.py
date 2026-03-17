import _sqlite3

DATABASE_NAME = "~/PIDashboard/sensordb.db"

conn = _sqlite3.connect(DATABASE_NAME)

cursor = conn.cursor()

