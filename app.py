from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adhesion', methods=['GET', 'POST'])
def adhesion():
    if request.method == 'POST':
        data = {
            'nom': request.form['nom'],
            'prenom': request.form['prenom'],
            'date_naissance': request.form['date_naissance'],
            'adresse': request.form['adresse'],
            'code_postal': request.form['code_postal'],
            'ville': request.form['ville'],
            'pays': request.form['pays'],
            'telephone': request.form['telephone'],
            'email': request.form['email']
        }

        # Sauvegarder dans un fichier CSV
        with open('demandes_adhesion.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

        return render_template('merci_adhesion.html', prenom=data['prenom'])

    return render_template('adhesion.html')

if __name__ == '__main__':
    app.run(debug=True)

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

