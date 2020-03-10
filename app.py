from flask import Flask, render_template, request

#from database import *

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template("index.html")

@app.route('/')
def paintings():
    
    return render_template("paintings.html")

@app.route('/')
def about():
    
    return render_template("about.html")

@app.route('/')
def contact():
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)