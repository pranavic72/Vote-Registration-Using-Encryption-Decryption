import mysql.connector
from main import decrypt,privKey
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cyber"    
    )
cursor = mydb.cursor()

id = input("Enter Voter ID: ")
cursor.execute("select * from voters where id="+id)

result=cursor.fetchone()
efname = result[1]
elname = result[2]
eemail = result[3]
ephone = result[4]
eaadhar = result[5]
evote = result[6]
fname = decrypt(efname,privKey)
lname = decrypt(elname,privKey)
email = decrypt(eemail,privKey)
phone = decrypt(ephone,privKey)
aadhar = decrypt(eaadhar,privKey)
vote = decrypt(evote,privKey)

print("*****Voter Details*****")
print("Name: "+fname+" "+lname)
print("Email: "+email)
print("Phone: "+phone)
print("Aadhar No: "+aadhar)
print("Vote: "+vote)
