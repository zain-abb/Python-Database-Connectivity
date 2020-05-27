import pymysql

# database connection
connection = pymysql.connect(
    host="localhost", user="root", passwd="", database="mydatabase")
cursor = connection.cursor()

# queries for retrievint all rows
retrive = "Select * from Artists;"

# executing the quires
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
    print(row)


# commiting the connection then closing it.
connection.commit()
connection.close()

# Update
# updateSql = "UPDATE  Artists SET NAME= 'Tauwang'  WHERE ID = '1' ;"
# cursor.execute(updateSql)

# Delete
# deleteSql = "DELETE FROM Artists WHERE ID = '1'; "
# cursor.execute(deleteSql)

# Drop Table
# dropSql = "DROP TABLE IF EXISTS Artists;"
# cursor.execute(dropSql)
