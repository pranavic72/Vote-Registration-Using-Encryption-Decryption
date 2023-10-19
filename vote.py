from urllib import request
from main import encrypt,pubKey,decrypt,privKey
from flask import Flask,render_template,request
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cyber"    
    )

@app.route('/')
@app.route('/register',methods=['POST','GET'])
def register():
    msg=""
    if request.method == 'POST':
        login = request.form
        fname=login['fname']
        lname=login['lname']
        email = login['email']
        phone=login['phone']
        aadhar=login['aadhar']
        vote=login['vote']
        cursor = mydb.cursor()

        fname = encrypt(fname,pubKey)
        lname = encrypt(lname,pubKey)
        email = encrypt(email,pubKey)
        phone = encrypt(phone,pubKey)
        aadhar = encrypt(aadhar,pubKey)
        vote = encrypt(vote,pubKey)
        
        cursor.execute("insert into voters(fname,lname,email,phone,aadhar,vote) values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,phone,aadhar,vote))
        mydb.commit()
        msg = "Successfully Logged in!"
    else:
        msg = "Failed! Try Again"
    return render_template('form.html',msg=msg) 
        
if __name__=="__main__": #to check we only run the page
    app.run(debug=True)