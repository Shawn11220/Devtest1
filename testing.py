from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Shawn!"

@app.route('/test')
def test():
    return "This is a test route!"

if __name__ == '__main__':
    app.run(debug=True)
