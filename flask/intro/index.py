from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "this is the basic template for flask"

def index():
    return "this is the index page"


if __name__ =="__main__":
    app.run(debug=True) #debug true makes so the changes show on web instantly without having to start the server again