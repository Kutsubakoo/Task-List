from flask import Flask, render_template

app = Flask(__name__)

tasklist = [["Walk Dog", True], ["Wash Dishes", False], ["Take out Trash", True]]
@app.route("/")
def home():
    return render_template("tasklist.html", TaskList=tasklist)

app.run()