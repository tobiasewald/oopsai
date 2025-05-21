from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, vulnerable world!!"

@app.route('/eval')
def evil():
    expr = request.args.get('input')
    return str(eval(expr))

if __name__ == '__main__':
    app.run(debug=True)
