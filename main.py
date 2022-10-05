import requests
from flask import Flask,render_template

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
    

@app.route('/contact')
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)
