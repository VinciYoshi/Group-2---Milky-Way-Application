from sqlite3 import *

# Creates the database
def createDatabase():
	conn = connect("database.db")
	c = conn.cursor()

	c.execute("""CREATE TABLE IF NOT EXISTS milkTable (
				id text,
				firstname text,
				lastname text,
				description text,
				expiry text,
				daysExpiry integer
			)

			""")
	conn.commit()
	conn.close()

# Add item to the database
def addProduct(pId, firstname, lastname, description, expiry, daysExpiry):
	conn = connect("database.db")
	c = conn.cursor()

	c.execute("INSERT INTO milkTable VALUES (:ID, :FIRSTNAME, :LASTNAME, :DESCRIPTION, :EXPIRY, :DAYSEXPIRY)",
		{
		"ID": pId,
		"FIRSTNAME": firstname,
		"LASTNAME": lastname,
		"DESCRIPTION": description,
		"EXPIRY": expiry,
		"DAYSEXPIRY": daysExpiry
		}
		)

	conn.commit()
	conn.close()

# Find product using search
def readProductFind(pId):
	conn = connect("database.db")
	c = conn.cursor()

	c.execute("SELECT * FROM milkTable WHERE id LIKE '{}'".format(pId))

	currentRow = c.fetchone()

	conn.commit()
	conn.close()

	return currentRow

# Reads the database and displays on a table
def readProductTable():
	conn = connect("database.db")
	c = conn.cursor()

	all = c.execute("SELECT * FROM milkTable")
	return all

	conn.commit()
	conn.close()

# Edit a data from database
def confirmEdit(pId, a, b, c, d, e):
	conn = connect("database.db")
	c2 = conn.cursor()

	c2.execute("""UPDATE milkTable SET
		firstname = '{}',
		lastname = '{}',
		description = '{}',
		expiry = '{}',
		daysExpiry = '{}'
		WHERE id LIKE '{}'
		""".format(a, b, c, d, e, pId))

	conn.commit()
	conn.close()

# Initializes the input fields for editing
def editShow(pId):
	conn = connect("database.db")
	c = conn.cursor()

	c.execute("SELECT * FROM milkTable WHERE id LIKE '{}'".format(pId))
	currentEdit = c.fetchone()

	conn.commit()
	conn.close()

	return currentEdit

# Deletes a row from a database
def deleteRow(pId):
	conn = connect("database.db")
	c = conn.cursor()

	c.execute("DELETE FROM milkTable WHERE id LIKE '{}'".format(pId))

	conn.commit()
	conn.close()

# Notifications warning expiries
def nExpiryWarningShow(n):
	conn = connect("database.db")
	c = conn.cursor()

	all = c.execute("""SELECT id, firstname, lastname FROM milkTable WHERE daysExpiry <= {}
		AND daysExpiry > 0""".format(n))
	return all

	conn.commit()
	conn.close()

# Notifications withdrawed products
def nWithdrawnShow(n):
	conn = connect("database.db")
	c = conn.cursor()

	all = c.execute("SELECT id, firstname, lastname FROM milkTable WHERE daysExpiry <= 0")
	return all

	conn.commit()
	conn.close()
