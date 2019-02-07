#import dependencies
from flask import Flask, render_template

#create instance
app = Flask(__name__)

#define route
@app.route("/")

#content
def home():
    return render_template("home.html")

#define 2 route
@app.route('/blog')
def about():
    return render_template("blog.html")

#runnig and controlling script
if(__name__ == "__main__"):
    app.run(debug=True)
