from flask import Flask
from flask_clova import Clova, question, statement

app = Flask(__name__)
clova = Clova(app, '/')

@clova.launch
def launch():
    return question('안녕하세요. 베스킨라빈스 게임입니다.').add_speech('신난다 재미난다 베스킨라빈스 게임').add_speech('일 이')


@clova.intent('HelloIntent')
def play_game():
    speech = "안녕하세요"
    return statement(speech).add_speech("Hello", lang='en')


@clova.intent('game', mapping={'number': 'num1'}, convert={'num1': int})
def play_game(num1):
    speech = "{}을 말씀하셨습니다.".format(num1)
    return statement(speech)


@clova.default_intent
def not_play_game():
    speech1 = "다른 말씀을 하시면 곤란합니다."
    speehc2 = "다시 시작하죠. 일 이"
    return question(speech1).add_speech(speehc2)


if __name__ == "__main__":
    app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.run(host='0.0.0.0', port='80')