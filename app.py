from flask import Flask, send_file
from tkinter.filedialog import  askopenfilename

app = Flask(__name__)

@app.route('/')
def index():
    return send_file(askopenfilename(),'r')

@app.route('/file')
def file():
    return send_file('requirements.txt')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)