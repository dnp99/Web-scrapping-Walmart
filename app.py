from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
      return 'Hello, Deep!'
@app.route('/app1/')
def hello_world():
      return 'Hello, Deep!'

if __name__ == "__main__":
    app.run()