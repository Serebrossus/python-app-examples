#import dependencies
from flask import Flask

#create instance
app = Flask(__name__)

#define route
@app.route("/")

#content
def home():
    return ("Home Page")

#runnig and controlling script
if(__name__ == "main"):
    app.run(debug=True)
