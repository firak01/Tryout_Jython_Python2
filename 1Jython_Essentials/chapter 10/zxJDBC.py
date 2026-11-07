import com.ziclix.python.sql as sql
dburl, user, pw, drv = ("jdbc:mysql://localhost/test", None, None, 
        "org.gjt.mm.mysql.Driver")
db = sql.zxJDBC.connect(dburl, user, pw, drv)

cursor = db.cursor()
cursor.datahandler = sql.handler.MySQLDataHandler(cursor.datahandler)
cursor.execute("""CREATE TABLE IF NOT EXISTS test (
    object_id integer primary key, 
    name varchar(100),
    grade float)""")
cursor.execute("DELETE FROM test")
cursor.executemany("""INSERT INTO TEST (object_id, name, grade) 
        VALUES (?, ?, ?)""",
        ((1, 'Fred Flintstone', 90.5), (2, 'Zach Paleozogt', 100)))
db.commit()
        
cursor.execute("SELECT * FROM TEST ORDER BY GRADE DESC")
print cursor.description    

print cursor.fetchall()

