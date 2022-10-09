import smtplib
import requests
from flask import Flask,render_template,request

my_email="regishshrestha@gmail.com"
password="dmreixqeuionlbxx"

app = Flask(__name__)
    

@app.route('/')
def home():
    response=requests.get("https://api.npoint.io/18aae9aafedc1b39590e")
    data=response.json()
    return render_template("index.html",all_data=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<id>')
def post(id):
    print(id)
    response=requests.get("https://api.npoint.io/18aae9aafedc1b39590e")
    datas=response.json()
    for data in datas:
        if int(data['id'])==int(id):
            data_got=data        
    return render_template("post.html",data=data_got)
    # return render_template("post.html")
    

@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html",msg_sent=False)
    else:
        name=request.form['name']  
        email=request.form['email']
        phone_number=request.form['phone_number']
        message=request.form['message']
        print(name,email,phone_number,message)
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="regishshrestha@gmail.com",             msg=f"Subject:New Message \n\n Name: {name} \n email: {email} \n Phone Number: {phone_number} \n Message: {message}")
        connection.close()
        return render_template("contact.html",msg_sent=True)
        


# @app.route('/form-entry',methods=['POST',"GET"])
# def receive_data():
#         name=request.form['name']
#         email=request.form['email']
#         phone_number=request.form['phone_number']
#         message=request.form['message']
#         print(name,email,phone_number,message)
#         if request.method == 'POST':
#             return "Sucessfully send the message"

if __name__ == "__main__":
    app.run(debug=True)
