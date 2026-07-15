from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE = "students.json"


# ---------- Load Data ----------
def load_students():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


# ---------- Save Data ----------
def save_students(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- Home ----------
@app.route("/")
def index():
    students = load_students()
    return render_template("index.html", students=students)


# ---------- Add ----------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        students = load_students()

        new_student = {
            "name": request.form["name"],
            "age": request.form["age"]
        }

        students.append(new_student)
        save_students(students)

        return redirect("/")

    return render_template("add.html")


# ---------- Edit ----------
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    students = load_students()

    if request.method == "POST":
        students[index]["name"] = request.form["name"]
        students[index]["age"] = request.form["age"]

        save_students(students)
        return redirect("/")

    return render_template("edit.html", student=students[index], index=index)


# ---------- Delete ----------
@app.route("/delete/<int:index>")
def delete(index):
    students = load_students()
    students.pop(index)
    save_students(students)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)