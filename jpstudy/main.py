from flask import Blueprint
from flask_clova import Clova, question, statement, session

app = Blueprint('jpstudy_api', __name__, url_prefix="/jpstudy")
clova = Clova(blueprint=app)


@clova.launch
def launch():
    return question('안녕하세요. 일본어 단어 공부를 시작해 볼까요?')\
        .add_speech('おはようございます あなたの日本語先生です。', lang='ja')\
        .add_speech('어떤 학습을 하고 싶으세요?')


@clova.intent('ihyungyoungsa')
def ihyungyoungsa():
    speech = "이 형용사를 공부해봅시다. 뜻을 말해보세요"
    word = make_question()
    session.sessionAttributes['play'] = 'ihyungyoungsa'

    return question(speech).add_speech(word, lang='ja').reprompt(word, lang='ja')


@clova.intent('dongsa')
def dongsa():
    speech = "동사는 준비중입니다. 이 형용사를 해보는건 어떤가요?"
    return question(speech)


from .words import words_set

@clova.intent('answer', mapping={'ans': 'answer'})
def answer(ans):
    attr = session.sessionAttributes
    ask_word = attr.get('word')
    usr_word = words_set.get(ans)
    if ask_word is None:
        return not_play_game()
    elif usr_word is None:
        return statement("단어 사전 미등록..")
    elif usr_word == ask_word:
        word = make_question()
        return question("정답입니다.").add_speech("이건 뭘까요?").add_speech(word, lang='ja').reprompt(word, lang='ja')
    else:
        return question("틀렸습니다. 다시 들어보세요.").add_speech(ask_word ,lang='ja').reprompt(ask_word, lang='ja')


@clova.intent('letmeknow')
def give_answer():
    attr = session.sessionAttributes
    ask_word = attr.get('word')
    if ask_word is None:
        return statement('물어본적이 없는데 어떻게 정답을 말하나요.').add_speech('서비스 종료합니다.')
    for key ,word in words_set.items():
        if word == ask_word:
            ans = key
            next_word = make_question()
            return question('정답은 ' + ans + '입니다. 다른 단어를 들려드릴게요').add_speech(next_word, lang='ja')
    return statement('착오가 있었네요 개발자 잘못입니다. ㅠ')

@clova.default_intent
def not_play_game():
    speech1 = "다른 말씀을 하시면 곤란합니다."
    attr = session.sessionAttributes
    ask_word = attr.get('word')
    if ask_word is None:
        ask_word = 'システム終了'

    return question(speech1).add_speech(ask_word, lang='ja').reprompt(ask_word, lang='ja')


import random

def make_question():
    random_words = random.choice(list(words_set.keys()))
    target_word = words_set.get(random_words)
    session.sessionAttributes['word'] = target_word
    return target_word