from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('언어선택.html')

@app.route('/자주묻는 질문_영어')
def english():
    return render_template('자주묻는 질문_영어.html')

@app.route('/자주묻는 질문_일본어')
def english1():
    return render_template('자주묻는 질문_일본어.html')

@app.route('/자주묻는 질문_중국어')
def english2():
    return render_template('자주묻는 질문_중국어.html')

@app.route('/자주묻는 질문_한국어')
def english3():
    return render_template('자주묻는 질문_한국어.html')

if __name__ == '__main__':
    app.run(debug=True)

