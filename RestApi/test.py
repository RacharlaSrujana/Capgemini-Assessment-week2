from flask import Flask,request,jsonify
from flask_cors import CORS
import mysql.connector

app=Flask(__name__)
CORS(app)

conn=mysql.connector.connect(host="localhost",user="root",password="Srujana2003$",database="test_api")
mycursor=conn.cursor()

# To get all users
@app.route('/employ', methods=['GET'])
def get_employees():
    mycursor.execute("select * from employee")
    emp=mycursor.fetchall()
    return jsonify(emp)

# To get user by age
@app.route('/employ/<int:age>',methods=['GET'])
def get_employess_by_age(age):
    mycursor.execute("select * from employee where age=%s",(age,))
    emp=mycursor.fetchall()
    if emp:
        return jsonify(emp)
    return jsonify({"message": "Employee of that age is not found"}), 404

# Return employees whose salary>50000
@app.route('/employ/<int:salary>',methods=['GET'])
def get_employess_by_salary(salary):
    mycursor.execute("select * from employee where salary>%s",(salary,))
    emp=mycursor.fetchall()
    if emp:
        return jsonify(emp)
    return jsonify({"message": "Employee of that age is not found"}), 404

# Return names and salary of employess of a particular department
@app.route('/employ/<string:department>',methods=['GET'])
def get_employess_by_department(department):
    mycursor.execute("select emp_name,salary from employee where department=%s",(department,))
    emp=mycursor.fetchall()
    if emp:
        return jsonify(emp)
    return jsonify({"message": "There is no such department"}), 404

# Order employees by salary
@app.route('/employ',methods=['GET'])
def employee_order():
    mycursor.execute("select * from employee order by salary")
    emp=mycursor.fetchall()
    return jsonify(emp)

if __name__=="__main__":
    app.run(debug=True)