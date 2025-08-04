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
    try:
        active_lections=request.form.getlist("Lektion[]")
        
        active_lections.sort(reverse=True)
        highest_lection = active_lections[0]
        highest_lection = int(highest_lection)
        print(type(highest_lection))

        print(active_lections)

        print(highest_lection)
        vocabs = checker.main(text,highest_lection)
        return render_template('index.html',vocabs=vocabs)
    except IndexError:
        print("ERROR:  Liste ist leer!! ")


def start_ui() -> None:
    threading.Timer(1.0, open_browser).start()
    app.run()

if __name__ == '__main__':
    # Browser in separatem Thread öffnen, um Flask nicht zu blockieren
    threading.Timer(1.0, open_browser).start()
    app.run()
