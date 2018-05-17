from flask import Blueprint, render_template
from flask_clova import Clova, question, statement, session

app = Blueprint('jpstudy_api', __name__, url_prefix="/jpstudy")
clova = Clova(blueprint=app)


@clova.launch
def launch():
    return question('안녕 일본어 공부를 시작해 볼까요?')\
        .add_speech('おはようございます あなたの日本語先生です。', lang='ja')\
        .add_speech('어떤 학습을 하고 싶으세요?')


@clova.intent('ihyungyoungsa')
def ihyungyoungsa():
    speech = "이 형용사를 공부해봅시다. 뜻을 말해보세요"
    word = "良い"
    session.sessionAttributes = {
        'word': word,
        'play': 'ihyungyoungsa'
    }

    return question(speech).add_speech(word, lang='ja')


@clova.intent('dongsa')
def dongsa():
    speech = "동사를 공부해봅시다. 뜻을 말해보세요"
    word = '見る'
    session.sessionAttributes = {
        'word': word,
        'play': 'dongsa'
    }

    return question(speech).add_speech(word, lang='ja')


@clova.intent('answer', mapping={'ans', 'answer'})
def answer(ans):
    attr = session.sessionAttributes
    ask_word = attr.get('word')
    usr_word = word_set.get(ans)
    if ask_word is None:
        return not_play_game()
    elif usr_word is None:
        return statement("단어 사전 미등록..")
    elif usr_word == ask_word:
        return statement("정답입니다.").add_speech("正解です", lang='ja')
    else:
        return question("틀렸습니다. 다시 들어보세요.").add_speech(ask_word ,lang='ja')


@clova.default_intent
def not_play_game():
    speech1 = "다른 말씀을 하시면 곤란합니다."
    return statement(speech1).add_speech('システム終了', lang='ja')


word_set = {
    '보다': '見る',
    '좋다': '良い'
}