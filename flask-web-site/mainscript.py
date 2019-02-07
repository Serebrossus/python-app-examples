#import dependencies
from flask import Flask

#create instance
app = Flask(__name__)

#define route
@app.route("/")

#content
def home():
    return ("Home Page")

#define 2 route
@app.route('/about')
def about():
    return ("About me")

#runnig and controlling script
if(__name__ == "__main__"):
    app.run(debug=True)
