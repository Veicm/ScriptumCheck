from flask import Flask,render_template,request
import webbrowser
import threading

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
    
    splitted_text = text.split(" ")

    print(splitted_text)
    vocabs=[
        {"vocab":  "Servus", "in_db":True},
        {"vocab":  "Servus", "in_db":True},
        {"vocab":  "Servus", "in_db":True},
        {"vocab":  "Servus", "in_db":True},
        {"vocab":  "Servus", "in_db":True}
    ] #<-------- Dictonary has to be filled with the result; So vocab + result(If it exists or not in the db)
    return render_template('index.html',vocabs=vocabs)





if __name__ == '__main__':
    # Browser in separatem Thread öffnen, um Flask nicht zu blockieren
    threading.Timer(1.0, open_browser).start()
    app.run()
