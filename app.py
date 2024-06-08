from flask import Flask, render_template, request, redirect, url_for,session
import firebase_admin
from firebase_admin import credentials, auth 
from google.oauth2 import id_token
from google.auth.transport import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify
cred = credentials.Certificate('D:/WEB/tutor/Tutor/tutor-d3287-firebase-adminsdk-yn4ih-e6d8f120eb.json')
firebase_admin.initialize_app(cred,{
    'clock_skew_seconds': 10  # Allow 10 seconds of clock skew
})
app = Flask(__name__)

import pyrebase

config = {
  "apiKey": "AIzaSyDsvm1XJc01hvnzA6u7iqDWSZlE2rX_QZA",
  "authDomain": "tutor-d3287.firebaseapp.com",
  "projectId": "tutor-d3287",
  "storageBucket": "tutor-d3287.appspot.com",
  "messagingSenderId": "556016258412",
  "appId": "1:556016258412:web:ece9c8a2782befd68c7749",
  "measurementId": "G-8YYSCZ3T5P",
  "databaseURL": "https://tutor-d3287-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
pyrebase_auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))

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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = pyrebase_auth.create_user_with_email_and_password(email=email, password=password)
            return redirect(url_for('index'))
        except Exception as e:
            error_message = str(e)
            return render_template('signup.html', error=error_message)

    return render_template('signup.html')


@app.route('/google-sign-in', methods=['POST'])
def google_sign_in():
    data = request.get_json()
    idtoken = data.get('token')
    
    print("Received ID token:", idtoken)
    try:
        import time,jwt
        current_time = int(time.time())
        print(f"Server time before verification: {current_time}")
        
        # Verify the ID token
        decoded_token = auth.verify_id_token(idtoken)
        print(f"Token iat: {decoded_token['iat']}, exp: {decoded_token['exp']}")
        print(f"Token claims: {decoded_token}")
        uid = decoded_token['uid']
        email = decoded_token.get('email', '')
        name = decoded_token.get('name', '')

        
        session['user'] = {
            'uid': uid,
            'email': email,
            'name': name
        }

        return jsonify({'success': True, 'redirect': url_for('dashboard')})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': str(e)})


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    user = session['user']
    return render_template('dashboard.html', user=user)



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)