import os
import uuid
import pandas as pd
from flask import Flask, render_template, request, Response, send_from_directory, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'GET':
                return render_template('index.html')
        elif request.method == 'POST':
                username = request.form.get('username')
                password = request.form.get('password')

                if username == 'neuralnine' and password == 'password':
                        return 'Success'
                else:
                        return 'Failed'
                
@app.route('/file_upload', methods=['POST'])
def file_upload():
        file = request.files['file']

        if file.content_type == 'text/plain':
                return file.read().decode()
        elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
                df = pd.read_excel(file)
                return df.to_html()

@app.route('/convert_csv', methods=['POST'])
def convert_csv():
        file = request.files['file']

        df = pd.read_excel(file)

        response = Response(
                df.to_csv(),
                mimetype='text/csv',
                headers={
                        'Content-Disposition': 'attachment; filename=result.csv'
                }
        )

        return response

@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
        file = request.files['file']

        df = pd.read_excel(file)

        if not os.path.exists('downloads'):
                os.makedirs('downloads')
        
        filename = f'{uuid.uuid4()}.csv'
        df.to_csv(os.path.join('downloads', filename))

        return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
        return send_from_directory('downloads', filename, download_name='result.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
        greeting = request.json['greeting']
        name = request.json['name']

        with open('file.txt', 'w') as f:
                f.write(f'{greeting}, {name}')

        return jsonify({'message': 'Successfully written!'})















@app.route('/other')
def other():
        some_text = 'Hello Worldfowinewofwe'
        return render_template('other.html', some_text=some_text)











# @app.template_filter('reverse_string')
# def reverse_string(s):
#         return s[::-1]

# @app.template_filter('repeat')
# def repeat(s, times=2):
#         return s * times

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