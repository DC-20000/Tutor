from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form.get('chooseSubject')
        grade = request.form.get('grade')
        question_type = request.form.get('typeOfQuestions')
        difficulty = request.form.get('difficulty')
        num_questions = request.form.get('numQuestions')
        topics_of_interest = request.form.get('topicsOfInterest')

        # Debug prints
        print("Subject:", subject)
        print("Grade:", grade)
        print("Type of Questions:", question_type)
        print("Difficulty:", difficulty)
        print("Number of Questions:", num_questions)
        print("Topics of Interest:", topics_of_interest)

        return redirect(url_for('test_page', subject=subject, grade=grade, question_type=question_type, difficulty=difficulty, num_questions=num_questions, topics_of_interest=topics_of_interest))

    return render_template('index.html')

@app.route('/test_page', methods=['GET'])
def test_page():
    subject = request.args.get('subject')
    grade = request.args.get('grade')
    question_type = request.args.get('question_type')
    difficulty = request.args.get('difficulty')
    num_questions = request.args.get('num_questions')
    topics_of_interest = request.args.get('topics_of_interest')

    return render_template('test_page.html', subject=subject, grade=grade, question_type=question_type, difficulty=difficulty, num_questions=num_questions, topics_of_interest=topics_of_interest)

@app.route('/result', methods=['GET'])
def result():
    subject = request.args.get('subject')
    grade = request.args.get('grade')
    question_type = request.args.get('question_type')
    difficulty = request.args.get('difficulty')
    num_questions = request.args.get('num_questions')
    topics_of_interest = request.args.get('topics_of_interest')

    return render_template('result.html', subject=subject, grade=grade, question_type=question_type, difficulty=difficulty, num_questions=num_questions, topics_of_interest=topics_of_interest)

if __name__ == '__main__':
    app.run(debug=True)