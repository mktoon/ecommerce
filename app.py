# Import required libraries
from flask import Flask, request, jsonify
import sqlite3
#User table schema
"""CREATE TABLE "User" (
	"userID"	INTEGER,
	"userName"	TEXT NOT NULL,
	"userPassword"	TEXT NOT NULL,
	"userPreferences"	TEXT,
	PRIMARY KEY("userID" AUTOINCREMENT)
)"""
#products bought table schema
"""CREATE TABLE "productsBought" (
	"userProductID"	INTEGER,
	"userID"	NUMERIC,
	"productID"	INTEGER,
	"userName"	INTEGER,
	"dateOfPurchase"	TEXT,
	FOREIGN KEY("productID") REFERENCES "Product"("productID"),
	FOREIGN KEY("userID") REFERENCES "User"("userID"),
	PRIMARY KEY("userProductID" AUTOINCREMENT)
)"""
#Product table schema
"""CREATE TABLE "Product" (
	"productID"	INTEGER,
	"name"	TEXT NOT NULL,
	"description"	TEXT,
	"manufacturerName"	TEXT,
	"inventoryCount"	INTEGER,
	PRIMARY KEY("productID" AUTOINCREMENT)
)"""

# Create Flask app
app = Flask(__name__)

# Database connection configuration
connection = sqlite3.connect('C:/Users/Mktoo/OneDrive/Desktop/cloudC/ecommerceDB.db')
cursor = connection.cursor()

# Define API endpoints

#PRE:
#POST: List all the products in the database
@app.route('/products', methods=['GET'])
def get_products():
    cursor.execute('SELECT * FROM Product')
    products = cursor.fetchall()
    return jsonify(products)

#PRE:
#POST: Add a new product to the database
@app.route('/products', methods=['POST'])
def addProduct():
    newProduct = request.json
    cursor.execute('INSERT INTO Product (name, description, manufacturerName, inventoryCount) VALUES (?, ?, ?, ?)',
                   (newProduct['name'], newProduct['description'], newProduct['manufacturerName'], newProduct['inventoryCount']))
    connection.commit()
    return jsonify(newProduct)
# PRE:
#POST: List all the users in the database
@app.route('/users', methods=['GET'])
def getUsers():
    cursor.execute('SELECT * FROM User')
    users = cursor.fetchall()
    return jsonify(users)

# PRE: 
# Post: add a new user to the database
@app.route('/users', methods=['POST'])  
def add_user():
    newUser = request.json
    cursor.execute('INSERT INTO User (userName, userPassword, userPreferences) VALUES (?, ?, ?)',
                   (newUser['userName'], newUser['userPassword'], newUser['userPreferences']))
    connection.commit()
    return jsonify(newUser)

#PRE:
#POST: List all the products bought in the database
@app.route('/productsBought', methods=['GET'])
def getProductsBought():
    cursor.execute('SELECT * FROM productsBought')
    productsBought = cursor.fetchall()
    return jsonify(productsBought)

#PRE: 
#POST: Add a new product bought to the database
@app.route('/productsBought', methods=['POST'])
def addProductBought():
    newProductBought = request.json
    cursor.execute('INSERT INTO productsBought (userID, productID, userName, dateOfPurchase) VALUES (?, ?, ?, ?)',
                   (newProductBought['userID'], newProductBought['productID'], newProductBought['userName'], newProductBought['dateOfPurchase']))
    connection.commit()
    return jsonify(newProductBought)

#PRE:
#POST: Delete products from the database by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(productID):
    cursor.execute('DELETE FROM Product WHERE productID = ?', (productID,))
    connection.commit()
    return jsonify({'message': 'Product deleted'})

#PRE: 
#POST: User Table API: DELETE a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def deleteUser(userID):
    cursor.execute('DELETE FROM User WHERE userID = ?', (userID,))
    connection.commit()
    return jsonify({'message': 'User deleted'})
#PRE:
#POST: Products Bought Table API: DELETE a product bought by ID
@app.route('/productsBought/<int:product_bought_id>', methods=['DELETE'])
def deleteProductBought(productBoughtID):
    cursor.execute('DELETE FROM productsBought WHERE userProductID = ?', (productBoughtID,))
    connection.commit()
    return jsonify({'message': 'Product bought deleted'})

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
    # Close the database connection
    connection.close()
    
