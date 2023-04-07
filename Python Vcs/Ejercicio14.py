import sqlite3

conn = sqlite3.connect('Students.db')
c = conn.cursor()

# c.execute("""CREATE TABLE students (
#               name TEXT,
#               last name TEXT,
#               years INTEGER
#         )""")

# c.execute("INSERT INTO students VALUES ('Juan Jose', 'Rojas Guaneme', 18)")
#
# todos_estudiantes = [
#      ('Juan Jose', 'Rojas Guaneme', 18),
#      ('Oscar David', 'Contreras Ochoa', 22),
#      ('Juan Esteban', 'Gil Merchan', 19),
#      ('Nicol Valeria', 'Rojas Aguedelo', 20),
#      ('Juan Manuel', 'Agudelo Castañeda', 19),
#      ('Jonathan', 'Martinez Ayala', 25),
#      ('Laura Maria', 'Quintero Rojas', 19),
#      ('Libby Daniel', 'Mosquera Ortiz', 17),
#
# ]

# c.executemany("INSERT INTO students VALUES (?, ?, ?)", todos_estudiantes)
c.execute("SELECT * FROM students")
x = c.fetchall()

for i in x:
    print(i)

conn.commit()
conn.close()
