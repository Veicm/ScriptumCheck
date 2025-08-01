from flask import Flask,render_template,request
import webbrowser
import threading
from backend.input_checker import InputChecker
checker = InputChecker()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

@app.route('/check',methods=["POST"])
def check_text(): # Checking Process in this function !!!
    text = request.form['text_input'] #   <------Text as string
    print(type(text))
    print(request.form.getlist("Lektion[]"))




    vocabs = checker.main(text)
    return render_template('index.html',vocabs=vocabs)



def start_ui() -> None:
    threading.Timer(1.0, open_browser).start()
    app.run()

if __name__ == '__main__':
    # Browser in separatem Thread öffnen, um Flask nicht zu blockieren
    threading.Timer(1.0, open_browser).start()
    app.run()
