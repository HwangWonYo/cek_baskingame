"""
    소라 고동님
    ~~~~~~~~

    소라 고동님은 모든 것을 정해줍니다.
"""
from flask import Blueprint
from flask_clova import Clova, question, statement


app = Blueprint('soragodong_api', __name__, url_prefix="/soragodong")
clova = Clova(blueprint=app)


import random
@clova.launch
def launch():
    return question(",").reprompt("응?")


@clova.default_intent
def default_intent():
    speech  = random.choice(dialog_set)
    return statement(speech)


@clova.intent('spare')
def nono():
    return


dialog_set = [
    "하지마",
    "가만히 있어",
    "그것도 안돼",
    "안돼",
    "다시 한번 물어봐",
    "그래",
    "좋아",
    "허락한다",
    "하도록 해",
    "그래",
    "그래",
    "굶어"
]