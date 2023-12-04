from flask import Flask, send_file
from tkinter.filedialog import  askopenfilename

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/file')
def file():
    open('ff.txt','w').write('Hello')
    return send_file('requirements.txt')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)