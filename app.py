from flask import Flask
from flask_clova import Clova, question, statement, session

app = Flask(__name__)
clova = Clova(app, '/')

@clova.launch
def launch():
    return question('안녕 베스킨라빈스 게임을 시작한다.')\
        .add_speech('신난다아 재미난다아 베스킨라빈스 게임')\
        .add_speech('일 이')\
        .reprompt("너 차례야. 일 이")


@clova.intent('game',
                mapping={'num1': 'numbera', 'num2': 'numbera', 'num3': 'numbera'},
                convert={'num1': int, 'num2': int, 'num3': int})
def play_game(num1, num2, num3):
    print(session)
    last_num = num3
    if last_num is None:
        last_num = num2
    if last_num is None:
        last_num = num3
    if last_num is None:
        last_num = num1

    if last_num >= 31 or last_num <= 0:
        return statement("내가 이겼다. 하하하.")
    if last_num == 30:
        return statement("내가 졌네.. 개발자가 잘못 만들었다.")

    speech_num  = make_number_to_speech(last_num)
    speech = speech_num
    if not speech:
        speech = str(last_num + 1)
    return question(speech).add_speech("이제 너 차례").reprompt("그만 할거야?")


def make_number_to_speech(last_num):
    if (last_num - 2) % 4 == 0:
        return ""
    speech = str(last_num + 1)
    return speech + " " + make_number_to_speech(last_num + 1)


@clova.default_intent
def not_play_game():
    print(session)
    speech1 = "다른 말씀을 하시면 곤란합니다."
    speehc2 = "처음부터 다시 시작하죠. 일 이"
    return question(speech1).add_speech(speehc2)


if __name__ == "__main__":
    app.config['CLOVA_VERIFY_REQUESTS'] = False
    app.run(host='0.0.0.0', port='80')