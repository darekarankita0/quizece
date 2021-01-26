import os
from helper import *
# import env # needed for development unittesting

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
score_data = 'data/scoreboard.txt'
riddle_json = 'data/riddle_data.json'


# Set the messages you want to appear when quiz is completed based on score,
# I defined this function in this file for easy editing by another developer
def get_final_score_message(score):
    message = ""
    if session['url'] > 10:
        if score < 3:
            message = "You scored " + str(session["score"]) + "/10. Terrible"
        elif score < 6:
            message = "You scored " + str(session["score"]) + "/10. Mediocre"
        elif score < 8:
            message = "You scored " + str(session["score"]) + "/10. Above average"
        elif score < 10:
            message = "You scored " + str(session["score"]) + "/10. Close... but no cigar"
        else:
            message = "You scored " + str(session["score"]) + "/10. You have mad Google skills"

    return message


# Login page to set session library of username and score
@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Take username input, strip of any whitespace and then run it through
        # the custom validation function.
        username = request.form['username'].strip()
        if username_validator(username) is False:
            flash("Username must contain between 3 and 10 characters and cannot contain any spaces")
        else:
            # Username is suitable therefore the session will be initiated
            # with this username"""
            initiate_session(username)
            return redirect(url_for('quiz'))
    return render_template("index.html")


# Login page to set session library of username and score  - for use with
# javascript supported browsers
@app.route('/js_login', methods=["GET", "POST"])
def js_login():
    if request.method == "POST":
        username = request.form['username'].strip()
        if username_validator(username) is False:
            flash("Username must contain between 3 and 10 characters and cannot contain any spaces")
            return render_template("index.html")
        else:
            initiate_session(username)
            total = questions_asked(session['url'])
            riddle = match_page_info_with_url(riddle_json, session['url'])
            return render_template("quiz_js.html", riddle=riddle, user=session,
                                   total=total)


# Render riddles with pictures and current score, dependant on progress.
@app.route('/quiz')
def quiz():
    total = questions_asked(session['url'])
    riddle = match_page_info_with_url(riddle_json, session['url'])
    # If 10 questions completed, the user will be taken to the leaderboard.
    if session['url'] > 10:
        return redirect('leaderboard')

    return render_template("member.html", riddle=riddle, user=session,
                           total=total)


# Validate riddle answers, adjust score, if answer incorrect flash message
# will display incorrect answer
# Will eventually redirect to leaderboard when all questions are
# answered or passed.
@app.route('/submit_answer', methods=["POST"])
def submit_answer():
    riddle = match_page_info_with_url(riddle_json, session['url'])
    if request.method == 'POST':
        guess = request.form['answer'].strip().title()
        answer = riddle["answer"]
        if session['url'] < 10:
            if guess == answer:
                increment_url_and_score(1, 1)
            else:
                flash('"{}" is incorrect. Please try again.'.format(
                      request.form['answer']))
        # If the user has answered 10 questions their score will be added to
        # the score board.
        elif session['url'] == 10:
            if guess == answer:
                increment_url_and_score(1, 1)
                add_to_scoreboard(session['username'], session['score'],
                                  score_data)
            else:
                flash('"{}" is incorrect. Please try again.'.format(
                      request.form['answer']))
        # If the user has been using the back button to try and cheat,
        # i.e. They go back and resubmit, their session[url] will remain
        # correct and they will redirected to the leaderboard if they have
        # answered 10 or more questions.
        else:
            return redirect('leaderboard')

        return redirect(url_for('quiz'))


# For js supporting browsers
# Validate riddle answers, adjust score, if answer incorrect flash message
# will display incorrect answer
# Will eventually redirect to leaderboard when all questions are answered.
# Javascript also removes alot of the issues with users using the back button
# to resubmit and cheat to get a higher total.
@app.route('/js_submit_answer', methods=["POST"])
def js_submit_answer():
    riddle = match_page_info_with_url(riddle_json, session['url'])
    if request.method == "POST":
        guess = request.form["answer"]
        guess = guess.strip().title()
        answer = riddle['answer']
        if session['url'] < 10:
            if guess == answer:
                increment_url_and_score(1, 1)
            else:
                flash('"{}" is incorrect. Please try again.'.format(
                      request.form['answer']))
        # If the user has answered 10 questions their score will be added
        # to the score board.
        elif session['url'] == 10:
            if guess == answer:
                increment_url_and_score(1, 1)
                add_to_scoreboard(session['username'], session['score'],
                                  score_data)
                scores = get_scoreboard_data(score_data)
                message = get_final_score_message(session['score'])
                return render_template('leaderboard_js.html', scores=scores,
                                       user=session, message=message)

            else:
                flash('"{}" is incorrect. Please try again.'.format(
                      request.form['answer']))

        total = questions_asked(session['url'])
        riddle = match_page_info_with_url(riddle_json, session['url'])
        return render_template("quiz_js.html", riddle=riddle, user=session,
                               total=total)


# Skip button included to pass question and yet increment the session url by 1
@app.route('/skip_question', methods=["POST"])
def skip_question():
    if request.method == 'POST':
        if session['url'] == 10:
            # The url is increased but not the score.
            increment_url_and_score(1, 0)
            # redirected to leaderboard if 10 questions have been attempted.
            add_to_scoreboard(session['username'], session['score'],
                              score_data)
            return redirect('leaderboard')
        else:
            # The url is increased but not the score.
            increment_url_and_score(1, 0)
    return redirect(url_for('quiz'))


# Skip button included to skip over question and still increment the
# session url by 1 - JS supported browsers
@app.route('/js_skip_question', methods=["POST"])
def js_skip_question():
    if request.method == "POST":
        if session['url'] == 10:
            increment_url_and_score(1, 0)
            add_to_scoreboard(session['username'], session['score'],
                              score_data)
            scores = get_scoreboard_data(score_data)
            message = get_final_score_message(session['score'])
            return render_template('leaderboard_js.html', scores=scores,
                                   user=session, message=message)
        else:
            increment_url_and_score(1, 0)
            total = questions_asked(session['url'])
            riddle = match_page_info_with_url(riddle_json, session['url'])
            return render_template("quiz_js.html", riddle=riddle, user=session,
                                   total=total)


# Display leaderboard
@app.route('/leaderboard')
def leaderboard():
    scores = get_scoreboard_data(score_data)
    # This message will only be displayed once user has completed quiz and
    # it will correspond with their score.
    message = get_final_score_message(session['score'])
    return render_template("leaderboard.html", scores=scores, user=session,
                           message=message)


@app.route('/leaderboard_no_login')
def leaderboard_no_login():
    scores = get_scoreboard_data(score_data)
    # No message as there has been no score set by the user.
    message = " "
    return render_template("leaderboard.html", scores=scores, user=session,
                           message=message)


@app.route('/js_leaderboard_no_login')
def js_leaderboard_no_login():
    scores = get_scoreboard_data(score_data)
    # No message as there has been no score set by the user.
    message = " "
    return render_template("leaderboard2_js.html", scores=scores, user=session,
                           message=message)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)