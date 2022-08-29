# Image file send to the Database
# Import the required modules
from pathlib import Path
import mysql.connector
import base64
from PIL import Image
import io
import os

# Create a connection
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="00000000",
	database="sedatabase" # Name of the database
)

# Create a cursor object
cursor = mydb.cursor()
# Image file retrive into folder
for imgFiles in Path("images").glob("*.png"):
	with open(imgFiles, 'rb') as img:
	 img = base64.b64encode(img.read())

# Sample data to be inserted
args = ('103', 'suriya', img)

# Prepare a query
query = 'INSERT INTO PROFILE VALUES(%s, %s, %s)'

# Execute the query and commit the database.
cursor.execute(query,args)
mydb.commit()
