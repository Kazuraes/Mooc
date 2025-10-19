from flask import Flask, render_template, request,redirect, url_for, session # on importe les fonctions flask necessaire
import json, os # on importe aussi la fonction json
app = Flask(__name__) # on fait une variable qui contient Flask
fichier = 'utilisateur.json' # on donne au variable fichier le contenu json
def lectureJson() : # on fait une fonction qui :
    if os.path.exists(fichier) : # verifie si le fichier existe
        with open(fichier, 'r', encoding='utf-8') as f : # si il existe bien alors on l'ouvre mode lecture
            return json.load(f) # transforme le JSON en dictionnaire Python
@app.route('/creer_une_page_html') # on fait une route flask avec le mots cle @app.route et on donne un nom
# ⚠ c'est obligatoire pour pouvoir aller sur une page
def creer_une_page_html() : 
    return render_template('creer_une_page_html.html') # fonction qui retourne la page.html ici il faut mettre rendre_template
@app.route('/') # ici c'est la page principal index.html qu'on l'utilisateur entre dans le site
def home() : 


    return render_template('index.html') # ici la fonction qui retourne index.html
@app.route('/inscrire', methods=['GET', 'POST']) # route pour le formulaire et la methode post ou get
def inscription() : 
    if request.method == 'POST' : # si la method est post alors
        prenom = request.form.get('prenom', '') # on recupere le prenom
        email = request.form.get('email', '') # l"email
        password = request.form.get('password', '') # et le mot de passe
        if os.path.exists(fichier) : # voir en haut pour cette proprieter
            with open(fichier, 'r', encoding='utf-8') as f :  # ici aussi voir en haut
                try : 
                    utilisateurs = json.load(f) # utilisateur contient le json transformer en dictionnaire Python
                except json.JSONDecodeError : # l'erreur json.JSONDecodeError se produit qu'on il y a
                    # une erreur dans le json ex: un virgule en trop ("age": 11,) erreur il y a une virgule
                    utilisateurs = [] # dans ce cas on refais une liste utilisateurs
        else : # sinon
            utilisateurs = [] # on fait une liste utilisateurs
        if any(u['email'] == email for u in utilisateurs) : # verifier les doublons si l'email est deja present
            return render_template('index.html', error='cette email est deja utiliser !') # alors renvoie une erreur
        # voir index.html la syntexte suivante (qui est du Jinja2) {% if error %} si erreur alors paragraphe rouge indiquant l'ereur
        # s'il y a pas de doublons on fait un dictionnaire qui contiens le prenom, email et mot de passe
        nouvelle_utilisateur = {
            'prenom' : prenom,
            'email' : email,
            'password' : password
        }
        utilisateurs.append(nouvelle_utilisateur) # et on l'ajoute ces infos dans utilisateurs
        with open(fichier, 'w', encoding='utf-8') as f : # on ouvre le json en mode ecriture
            json.dump(utilisateurs, f, indent=4, ensure_ascii=False) # on ajoute utilisateurs dans le json
           # ensure_ascii=False : permet d’afficher les caractères spéciaux (é, à, 漢字…) sans les convertir en \uXXXX
           # ensure_ascii=True  (valeur par défaut) : convertit tout caractère non-ASCII en séquence \uXXXX
    return redirect(url_for('creer_une_page_html'))# des que tout est envoier email prenom password alors on renvoie vers la page.html
@app.route('/login', methods=['GET', 'POST']) # ici c'est pour la connexion methods post et get
def connexion() : 
    if request.method == 'POST' : # si la method post alors
        email = request.form.get('email', '').strip() # on verifie si email est pas vide 
        # la fonctio .strip() sert a annuler les espace et caractere speciaux
        password = request.form.get('password', '').strip()
        utilisateurs = lectureJson() # voir la fonction lecturejson() en haut
        if not utilisateurs : # si le json est vide alors
            utilisateurs = [] # on fait une liste dans le json
        for utilisateur in utilisateurs : # on parcours tout le json
            # si l'email est pareil a un email dans le json et que password est pareil a un passxord json alors
            if utilisateur.get('email') == email and utilisateur.get('password') == password :
                return redirect(url_for('creer_une_page_html')) # alors on renvoie vers creer_une_page_html.html
        return render_template('login.html', error='Email ou mot de passe incorrect') # si un dés 2 n'est pas bon alors erreur
    return render_template('login.html') # et on affiche la page login.html

@app.route('/organiser_votre_texte') # route vers organiser_votre_texte
def organiser_votre_texte() : 
    return render_template('organiser_votre_texte.html') # on renvoie vers la organiser_votre_texte.html

@app.route('/creer_un_lien_hypertexte_en_html') # route vers creer_un_lien_hypertexte_en_html
def creer_un_lien_hypertexte_en_html() : 
    return render_template('creer_un_lien_hypertexte_en_html.html') # on renvoie vers la creer_un_lien_hypertexte_en_html.html

@app.route('/inserer_des_images') # route vers inserer_des_images
def inserer_des_images() : 
    return render_template('inserer_des_images.html') # on renvoie vers la inserer_des_images.html
# if __name__ == "__main__" : exécute ce code seulement si on lance ce fichier directement (pas en import)
@app.route('/page4')
def page4() :
    return render_template('page4.html')
@app.route('/quiz_html') # route vers le quiz css
def quiz_html() :
    return render_template('quiz_html.html') 
@app.route('/quiz_css') # route vers le quiz html
def quiz_css() :
    return render_template('quiz_css.html')

if __name__ == '__main__' : 
    # app.run(debug=True) : démarre le serveur Flask en mode debug (rechargement auto + erreurs détaillées)
    app.run(debug=True)
