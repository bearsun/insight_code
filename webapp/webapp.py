from flask import Flask, render_template, request
from joblib import load
# Create the application object
app = Flask(__name__)
tfidf = load('tfidf.joblib')
tfidf_nb_app = load('tfidf_nb_app.joblib')

@app.route('/') #we are now using these methods to get user input
def home_page():
	return render_template('index.html', team1 = 'NBA',
      team2 = 'NBA', team3 = 'NBA')  # render a template

@app.route('/output', methods=['GET', 'POST'])
def home_post():
#  	 
  text = request.args.get('user_input')
  # Case if empty
  if text =='':
    return render_template("index.html", team1 = 'NBA',
      team2 = 'NBA', team3 = 'NBA')
  else:
    ptext = tfidf.transform([text])
    probs = tfidf_nb_app.predict_proba(ptext)
    ktop3 = probs[0].argsort()[-3:][::-1]
    teams = tfidf_nb_app.classes_[ktop3]
    prob3 = list(probs[0][ktop3]*100)
    return render_template("index.html", team1 = teams[0],
      team2 = teams[1], team3 = teams[2],
      prob1 = round(prob3[0], 2), prob2 = round(prob3[1], 2),
      prob3 = round(prob3[2], 2))


# start the server with the 'run()' method
if __name__ == "__main__":
	app.run(debug=True)
