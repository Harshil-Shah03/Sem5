import mysql.connector as msc
cnx = msc.connect(user="root", password="Apocalypse@123", host="127.0.0.1",database="harshil")
cursor = cnx.cursor()

# cursor.execute("CREATE TABLE student(id int(20),"
#                "                      fname varchar(20),"
# #                "                       lname varchar(20));")
# cursor.execute("show tables;")
# cursor.execute("insert into student values(128,'Ayush','Shah');")
# cursor.execute("insert into student values (129,'Ayush','Shah');")
# cursor.execute("insert into student values (130,'Ayush','Shah');")
# cursor.execute("Select * from student;")
result = cursor.fetchall()
for x in result:
    print(x)

cnx.commit()


