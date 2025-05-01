import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "student"

# Create a connection
connection = mysql.connector.connect(
host=host,
user=user,
password=password,
database=database
)

# Create a cursor object
cursor = connection.cursor()
# Execute a SELECT query
cursor.execute("SELECT * FROM applicants")
# Fetch all rows from the result
results = cursor.fetchall()
for row in results:
 print(row)
# Close the cursor
cursor.close()
# Close the connection
connection.close()