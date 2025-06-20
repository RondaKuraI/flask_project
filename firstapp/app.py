from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
        mylist = [10, 20, 30, 40, 50]
        return render_template('index.html', mylist=mylist)

@app.route('/other')
def other():
        some_text = 'Hello Worldfowinewofwe'
        return render_template('other.html', some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
        return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
        return s * times

# @app.route('/hello', methods=['GET', 'POST'])
# def hello():
#         if request.method == 'GET':
#                 return 'You made a GET request'
#         elif request.method == 'POST':
#                 return 'You made a POST request'
#         else:
#                 return "You will not see this message."

# @app.route('/greet/<name>')
# def greet(name):
#         return f"Hello {name}"

# @app.route('/add/<int:number1>/<int:number2>')
# def add(number1, number2):
#         return f'{number1} + {number2} = {number1 + number2}'

# @app.route('/handle_url_params')
# def handle_params():
#         if 'greeting' in request.args.keys() and 'name' in request.args.keys():
#                 greeting = request.args['greeting']
#                 name = request.args.get('name')
#                 return f'{greeting}, {name}'
#         else:
#                 return 'Some parameters are missing.'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)