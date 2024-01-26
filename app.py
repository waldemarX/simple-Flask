from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "secret_key"


# connect to database
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("landing.html")


@app.route("/adm_login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user and user["password"] == hashed_password:
            session["user_id"] = user["id"]
            return redirect(url_for("admin_panel"))
        else:
            error = "Invalid login or password"

    return render_template("login_adm.html", error=error)


@app.route("/admin_panel")
def admin_panel():
    if "user_id" not in session:
        return redirect(url_for("admin_login"))
    return render_template("admin_panel.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
