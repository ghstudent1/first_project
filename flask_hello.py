from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! test build works using pipeline SCM!!!!"

if __name__ == "__main__":
    app.run()





