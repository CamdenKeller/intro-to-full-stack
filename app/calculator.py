from flask import (
    Blueprint, render_template, request, redirect, g, flash
)
from app.db import get_db
import sqlite3

bp = Blueprint("calculator", __name__)

@bp.route("/addition", methods = ("GET", "POST"))
def addition():
    solution = None
    if request.method == "POST":
        try:
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            solution = num1 + num2

            db = get_db()
            db.execute(
                "INSERT INTO calculations (num1, num2, operand, solution) VALUES (?, ?, ?, ?)",
                (num1, num2, "addition", solution))
            db.commit()
        except (ValueError, KeyError) as e:
            flash(f"Error: {str(e)}")
        except sqlite3.IntegrityError:
            flash("This calculation has already been done")
        except Exception as e:
            flash(f"An error occurred: {str(e)}")

    return render_template("calculator/addition.html", solution=solution)

@bp.route("/multiplication", methods = ("GET", "POST"))
def multiplication():
    solution = None
    if request.method == "POST":
        try:
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            solution = num1 * num2

            db = get_db()
            db.execute(
                "INSERT INTO calculations (num1, num2, operand, solution) VALUES (?, ?, ?, ?)",
                (num1, num2, "multiplication", solution))
            db.commit()
        except (ValueError, KeyError) as e:
            flash(f"Error: {str(e)}")
        except sqlite3.IntegrityError:
            flash("This calculation has already been done")
        except Exception as e:
            flash(f"An error occurred: {str(e)}")

    return render_template("calculator/multiplication.html", solution=solution)

@bp.route("/history")
def history():
    db = get_db()

    calculations = db.execute("SELECT num1, num2, operand, solution FROM calculations").fetchall()

    return render_template("calculator/history.html", calculations = calculations)
    


