from flask import Flask, render_template, request
import datetime
import json

app = Flask(__name__)

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
    data = {
        'messages' : messages
    }
    # db = open(DB_FILE, 'w')
    # json.dump(data, db)
    # db.close()
    with open(DB_FILE, 'w') as db:
        json.dump(data, db)

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
    if len(name) < 3 or len(name) > 100:
        text = 'ERROR: Имя должно быть не короче 3 и не длиннее 100 символов'
    if len(text) < 1 or len(text) > 3000:
        text = 'ERROR: Текст должен быть не короче 1 и не длинее 3000 символов'
    add_message(text, name)
    return 'Ok'


DB_FILE = './data/db.json'
# db = open(DB_FILE, 'rb')
# data = json.load(db)
# db.close()
with open(DB_FILE, 'rb') as db:
    data = json.load(db)
messages = data['messages']

app.run()