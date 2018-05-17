from flask import Flask
from flask_clova import Clova, question, statement

app = Flask(__name__)
clova = Clova(app, '/')

@clova.launch
def launch():
    return question('시작했습니다')

@clova.intent('HelloIntent')
def play_game():
    speech = "안녕하세요"
    return statement(speech).add_speech("Hello", lang='en')


if __name__ == "__main__":
    app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.run(host='0.0.0.0', port='80')