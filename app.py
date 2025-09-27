from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

association_name = "Djama Guinee e.V"

@app.route("/")
def home():
    return render_template("index.html", association=association_name)

@app.route("/adhesion", methods=["GET", "POST"])
def adhesion():
    if request.method == "POST":
        nom = request.form.get("nom")
        email = request.form.get("email")
        telephone = request.form.get("telephone")
        message = request.form.get("message")

        # Pour l’instant on affiche juste dans la console
        print(f"Demande d'adhésion de {nom} ({email}, {telephone}): {message}")

        return redirect(url_for("merci_adhesion"))
    return render_template("adhesion.html", association=association_name)

@app.route("/merci-adhesion")
def merci_adhesion():
    return render_template("merci_adhesion.html", association=association_name)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)
association_name = "Djama Guinee e.V"

@app.route("/")
def home():
    return render_template("index.html", association=association_name)

@app.route("/adhesion", methods=["GET", "POST"])
def adhesion():
    if request.method == "POST":
        nom = request.form.get("nom")
        email = request.form.get("email")
        telephone = request.form.get("telephone")
        message = request.form.get("message")

        # Enregistrer dans un fichier CSV
        with open("adhesions.csv", "a", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow([nom, email, telephone, message])

        return redirect(url_for("merci_adhesion"))
    return render_template("adhesion.html", association=association_name)

@app.route("/merci-adhesion")
def merci_adhesion():
    return render_template("merci_adhesion.html", association=association_name)

if __name__ == "__main__":
    app.run(debug=True)

