import requests
from flask import Flask,render_template

app = Flask(__name__)
    
response=requests.get("https://api.npoint.io/18aae9aafedc1b39590e")
data=response.json()

@app.route('/')
def home():
    return render_template("index.html",all_data=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)
