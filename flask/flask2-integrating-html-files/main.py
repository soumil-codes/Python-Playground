from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html>" \
    "<h1>this is heading</h1><br>" \
    "<p>this is para</p>" \
    "<a href='/index'>landing page</a> <br>" \
    "<a href='/about'>about page</a>" \
    "</html>"

@app.route("/index")
def index():
    return render_template("index.html") #this will search inside templates folder

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ =="__main__":
    app.run(debug=True) 