from flask import Flask, Blueprint
from flask_clova import Clova, question, statement, session

app = Blueprint('bsrabins_api', __name__, url_prefix="/bsrabins")
clova = Clova(blueprint=app)


@clova.launch
def launch():
    session.sessionAttributes = {
        'turn_num': '3'
    }
    return question('안녕 베스킨라빈스 게임을 시작합니다.')\
        .add_speech('하나, 둘')\
        .reprompt("당신 차례입니다.일, 이")


@clova.intent('game',
                mapping={'num1': 'numbera', 'num2': 'numbera', 'num3': 'numbera'},
                convert={'num1': int, 'num2': int, 'num3': int})
def play_game(num1, num2, num3):
    print(session)
    turn_num = get_turn_num()

    last_num = num3
    if last_num is None:
        last_num = num2
    if last_num is None:
        last_num = num3
    if last_num is None:
        last_num = num1

    if last_num - turn_num > 2 or last_num - turn_num < 0:
        return question('규칙에 어긋납니다. 다시 해주세요.').add_speech(turn_num + "을 말할 차례입니다.")

    if last_num >= 31 or last_num <= 0:
        return statement("제가 이겼네요. 하하하.")
    if last_num == 30:
        return statement("제가 졌네요.. 개발자가 잘못만들었다.")

    speech_num  = make_number_to_speech(last_num)
    speech = speech_num
    if not speech:
        speech = str(last_num + 1)
    return question(speech).add_speech("이제 너 차례").reprompt("그만 할거야?")


@clova.default_intent
def not_play_game():
    print(session)
    speech1 = "다른 말씀을 하시면 곤란합니다."
    turn_num = get_turn_num()
    return question(speech1).add_speech(turn_num + "을 말씀하실 차례입니다.")


def get_turn_num():
    attr = session.sessionAttributes
    turn_num = attr.get('turn_num')
    return turn_num


def make_number_to_speech(last_num):
    if (last_num - 2) % 4 == 0:
        return ""
    speech = str(last_num + 1)
    return speech + " " + make_number_to_speech(last_num + 1)