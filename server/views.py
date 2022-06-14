from copyreg import pickle
from flask import Blueprint, render_template, request, flash


import nltk
from nltk.corpus import stopwords
import string, pickle

nltk.download('stopwords')

#loading classifier from pickle 
with open("models/classifier.pkl", "rb") as f:
    classifier = pickle.load(f)


#loading cv from picle 
with open("models/vectorizer.pkl", "rb") as v:
    cv = pickle.load(v)

#processing and tokenizing 
def process(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)

    clean = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean


views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        subject = request.form["SUB"]
        content = request.form["CON"]
        text = subject + content
        processed_text = process(text)
        vectorized_text = cv.transform(processed_text)
        flag = classifier.predict(vectorized_text)[0]
        if flag == 1:
            flash("This is a SPAM email.")
            print("spam")
            return render_template("base.html", flag = flag)
        elif flag == 0:
            flash("This is a HAM email.")
            print("ham")
            return render_template("base.html", flag = flag)
    print("get")        
    return render_template("base.html")
