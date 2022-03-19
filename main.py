from flask import Flask, render_template, request
import datetime
import json

def add_message(text, sender):
    now = datetime.datetime.now() # RAW Current Time
    current_time = now.strftime('%Y.%m.%d %H:%M:%S')
    new_message = {
        'text': text,
        'sender' : sender,
        'time' : current_time
    }
    messages.append(new_message)
    save_messages_to_file()

def save_messages_to_file():
    db = open(DB_FILE, 'w')
    data = {
        'messages' : messages
    }
    json.dump(data, db)
    db.close()

def print_message(message):
    print(f'{message["sender"]}: {message["text"]} / {message["time"]}')

# Главная страница
@app.route('/')
def index_page():
    return 'Здравствуйте, вас приветствует Скиллчат 2022'

# Показать все сообщения в формате json
@app.route('/get_messages')
def get_messages():
    return {'messages' : messages}

# показать форму чата
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/send_message')
def send_message():
    # получить из браузера имя и текст
    name = request.args['name']
    text = request.args['text']
    if 3 > len(name) > 100 or 1 > len(text) > 3000:
        return 'Error'
    add_message(text, name)
    return 'Ok'

app = Flask(__name__)

DB_FILE = './data/db.json'
db = open(DB_FILE, 'rb')
data = json.load(db)
db.close()
messages = data['messages']

app.run()