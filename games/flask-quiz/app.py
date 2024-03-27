from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

questions = [
    "Which would you rather eat?",
    "What animal would you rather have as a pet?",
    "What superpower would you rather have?",
    "Who would you rather have as a parent?",
    "What toast are you?",
]

cats = ["images/angrycat.jpg", "images/fatcat.jpg", "images/happycat.jpg", "images/sleepycat.jpg"]


@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    picture = None

    if request.method == 'POST':
        answers = [request.form.get(str(i)) for i in range(1, 6)]

        return redirect(url_for('result'))

    return render_template('quiz.html', questions=questions, picture=picture)


@app.route("/result")
def result():
    picture = random.choice(cats)
    return render_template('result.html', picture=picture)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


