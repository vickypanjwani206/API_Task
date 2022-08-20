from flask import Flask,jsonify
import pymongo
import mysql.connector


app=Flask(__name__)

################# Mongodb connection ##############
client=pymongo.MongoClient('mongodb://localhost:27017')
db=client['api_practice']

################# SQL Connection ##################
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vicky@9007"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("CREATE TABLE customers (name VARCHAR(50), address VARCHAR(50))")


################### Mongodb crud operations #############################

@app.route('/insert',methods=['GET','POST'])
def mongoInsert():
    db.student.insert({'roll_no':101,'name':"bharat",'class':10})
    response="Data inserted successfully"
    return jsonify(response)

@app.route('/read',methods=['GET','POST'])
def mongoRead():
    response=db.student.find({})
    return jsonify(response)

@app.route('/update',methods=['GET','POST'])
def mongoUpdate():
    db.student.update_one({'roll_no':101},{"$set":{'name':"vicky",'class':10}})
    response="Data updated successfully"
    return jsonify(response)

@app.route('/delete',methods=['GET','POST'])
def mongoDelete():
    db.student.delete_one({'roll_no':101})
    response="Data deleted successfully"
    return jsonify(response)

#################### SQL crud operations ######################

@app.route('/insertsql',methods=['GET','POST'])
def sqlInsert():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Vicky", "Khamgaon")
    mycursor.execute(sql, val)
    mydb.commit()
    response="SQL Data inserted successfully"
    return jsonify(response)

@app.route('/readsql',methods=['GET','POST'])
def sqlRead():
    mycursor.execute("SELECT * FROM customers")
    response = mycursor.fetchall()
    return jsonify(response)

@app.route('/updatesql',methods=['GET','POST'])
def sqlUpdate():
    sql = "UPDATE customers SET address = 'Khamgaon, Maharashtra' WHERE address = 'Khamgaon'"
    mycursor.execute(sql)
    mydb.commit()
    response="Data updated successfully"
    return jsonify(response)

@app.route('/deletesql',methods=['GET','POST'])
def sqlDelete():
    sql = "DELETE FROM customers WHERE address = 'Khamgaon'"
    mycursor.execute(sql)
    mydb.commit()
    response="Data deleted successfully"
    return jsonify(response)

if __name__=="__main__":
    app.run()