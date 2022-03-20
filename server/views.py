from flask import Blueprint, render_template, request, flash


views = Blueprint("views", __name__)

@views.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        subject = request.form["SUB"]
        content = request.form["CON"]
        print(subject, content)
    
    return render_template("base.html")
