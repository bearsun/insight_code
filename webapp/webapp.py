from flask import Flask, render_template, request
from joblib import load
# Create the application object
app = Flask(__name__)
tfidf = load('tfidf.joblib')
tfidf_nb_app = load('tfidf_nb_app.joblib')
cla = tfidf_nb_app.classes_

@app.route('/') #we are now using these methods to get user input
def home_page():
	return render_template('index.html')  # render a template

@app.route('/output', methods=['GET', 'POST'])
def home_post():
#  	 
  text = request.args.get('user_input')
  # Case if empty
  if text =='':
    return render_template("index.html", team = '')
  else:
    ptext = tfidf.transform([text])
    pred_team = tfidf_nb_app.predict(ptext)[0]
    return render_template("index.html", team = pred_team)


# start the server with the 'run()' method
if __name__ == "__main__":
	app.run(debug=True) #will run locally http://127.0.0.1:5000/