from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "rps_secret_key"   # required for session

choices = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}
@app.route("/", methods=["GET", "POST"])
def game():

    # initialize scores
    if "user_score" not in session:
        session["user_score"] = 0
        session["computer_score"] = 0

    user_choice = None
    computer_choice = None
    result = ""

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(list(choices.keys()))

        if user_choice == computer_choice:
            result = "It's a Tie 🤝!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win 🎉!"
            session["user_score"] += 1
        else:
            result = "Computer Wins 💻!"
            session["computer_score"] += 1

    return render_template(
        "page.html",
        user=user_choice,
        computer=computer_choice,
        result=result,
        emojis=choices,
        user_score=session["user_score"],
        computer_score=session["computer_score"]
    )
@app.route("/reset")
def reset():
    session["user_score"] = 0
    session["computer_score"] = 0
    return redirect(url_for("game"))

if __name__ == "__main__":
    app.run(debug=True)
