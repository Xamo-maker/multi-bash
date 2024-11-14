import tkinter as tk
import webbrowser
import time
import cmd
import urllib.request
import random
import os
import subprocess
import sys

# variable au lancement
launch_time = time.asctime()

# Classe de commandes
class Shell(cmd.Cmd):
    prompt = ""  # Pas de prompt car géré par l'interface Tkinter
    
    def do_help(self, arg, ):
        #Affiche la liste des commandes disponibles
        return('''Commandes disponibles: openurl [url], version, exit, clear, currentTime, launchTime, pipInstall [package], calc (calcul), openGitHub [profil] [reposit], helpPython, helpVsCode, helpNotepad, genPassword, helpSublimeText, creator''')

    def do_installPython(self, arg):
        url = "https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe"
        filename = "python-3.13.0-amd64"
        try:
            urllib.request.urlretrieve(url, filename)
            return("le ficher est normalement en téléchargement sous le nom de {filename}")
        except Exception as e:
            return("erreur lors du téléchargement")
        
    def do_installPythonWeb(self, arg):
        url = "https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe"
        webbrowser.open(url)
        return("lien ouvert")

    def do_currentTime(self, arg):
        #Affiche l'heure actuelle
        return(time.asctime())

    def do_launchTime(self, arg):
        #Affiche le temps de lancement de l'application
        return(launch_time)

    def do_version(self, arg):
        #Affiche la version de l'application
        return("Version actuelle: v0.5~py3.13\nlaunch time: {launch_time}")

    def do_bonjour(self, arg, line):
        command_history.append(line)
        #Affiche un message de bienvenue
        return("Hello, world!")

    def do_python(self, arg):
        #Exécute une commande Python 
        try:
            exec(arg)
            return("Commande Python exécutée.")
        except Exception as e:
            return("Erreur: {e}")
        
    def do_openurl(self, url):
        #Ouvre un URL spécifié 
        try:
            webbrowser.open(url)
            return("Ouvrir le lien : {url}")
        except Exception as e:
            return("Erreur lors de l'ouverture du lien : {e}")

    def do_openGitHub(self ,line, profil="", repos=""):
        command_history.append(line)
        url = f"https://github.com/{profil}/{repos}"
        try:
            webbrowser.open(url)
            return("ouverture du lien")
        except Exception as e:
            return("erreur lors de l'ouveture du lien")

    def do_exit(self, arg):
        #Ferme l'application
        root.destroy()

    def do_helpPython(self, arg):
        return '''commande impliquand python:
installPython
installPythonWeb
python [] (executer une commande python)
pythonWeb (ourvre python.org)'''

    def do_pythonWeb(self, arg):
        try:
            url = "https://python.org/"
            webbrowser.open(url)
            return("ouverture du site")
        except Exception as e:
            return "erreur lors de l'ouverture du lien : {e}"

    def do_print(self, exe):
        return exe

    def do_helpVsCode(self, arg):
        return '''commande impliquand VsCode
installCode
installCodeWeb'''

    def do_installCode(self, arg):
        url = "https://code.visualstudio.com/docs/?dv=win64user"
        filename = "VSCodeUserSetup.exe"
        try:
            urllib.request.urlretrieve(url, filename)
            return("le ficher est normalement en téléchargement sous le nom de {filename}")
        except Exception as e:
            return("erreur lors du téléchargement")

    def do_installCodeWeb(self, arg):
        url = "https://code.visualstudio.com/docs/?dv=win64user"
        webbrowser.open(url)
        return("lien ouvert")

    def do_helpSublimeText(self, arg):
        return '''installSublimeText
installSublimeTextWeb'''

    def do_installSublimeText(self, arg):
        url = "https://www.sublimetext.com/download_thanks?target=win-x64"
        filename = "sublime_text_build_setup.exe"
        try:
            urllib.request.urlretrieve(url, filename)
            return("le ficher est normalement en téléchargement sous le nom de {filename}")
        except Exception as e:
            return("erreur lors du téléchargement")

    def do_installSublimeTextWeb(self, arg):
        webbrowser.open("https://www.sublimetext.com/download_thanks?target=win-x64")
        return 'lien ouvert'

    def do_genPassword(self, arg,):
        result = subprocess.run(['node', 'generate_password.js'], capture_output=True, text=True)
        
        # Récupère le mot de passe généré depuis la sortie
        if result.returncode == 0:
            return(f"Mot de passe généré : {result.stdout.strip()}")
        else:
            return(f"Erreur lors de l'exécution du script : {result.stderr}")

    def do_helpNotepad(self):
        return '''installNotepad
installNotepadWeb'''

    def do_installNotepad(self, arg):
        url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.7.1/npp.8.7.1.Installer.x64.exe"
        filename = "npp.8.7.1.installer.x64.exe"
        try:
            urllib.request.urlretrieve(url, filename)
            return("le ficher est normalement en téléchargement sous le nom de {filename}")
        except Exception as e:
            return("erreur lors du téléchargement")
    def do_installNotepadWeb(self, arg):
        webbrowser.open("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.7.1/npp.8.7.1.Installer.x64.exe")
        return "lien ouvert"

    def do_creator(self):
        return '''name: Xamo-maker
github: https://github.com/Xamo-maker
languages: Français
technologie principal: Python, html, css
bio: un petit programmeur qui debute(depuis des années)'''

    def do_calc(self, expression):
        try:
            result = eval(expression)
            return f"{expression} : {result}"
        except Exception as e:
            return f"erreur dans l'expression : {e}"

    def do_clear(self, arg):
        text_zone.delete(1.0, tk.END)  # Efface le texte de la zone d'affichage
        return "Console nettoyée"

    def do_pipInstall(self, arg):
        """Installe le package spécifié via pip."""
        try:
            # Exécute la commande pip install pour le package spécifié avec le même exécutable Python
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", arg],
                capture_output=True,
                text=True
            )
            # Vérifie si l'installation a réussi
            if result.returncode == 0:
                return f"Le package '{arg}' a été installé avec succès."
            else:
                return f"Erreur lors de l'installation de '{arg}': {result.stderr}"
        except Exception as e:
            return f"Une erreur s'est produite : {e}"

    def default(self):
        #Commande par défaut pour les entrées non reconnues
        return("Commande inconnue ou syntaxe incorrecte.")


# Interface graphique
root = tk.Tk()
root.title("multi-bash v0.5")

# Créer un cadre pour contenir la zone de texte et la scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Créer une zone de texte pour afficher les résultats
text_zone = tk.Text(frame, width=60, height=20, wrap="word", bg="black", fg="white")
text_zone.pack(side="left", fill="both", expand=True)

# Créer une barre de défilement
scrollbar = tk.Scrollbar(frame, command=text_zone.yview)
scrollbar.pack(side="right", fill="y")

# Configurer la zone de texte pour utiliser la scrollbar
text_zone.config(yscrollcommand=scrollbar.set)

# Zone d'entrée pour taper la commande
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

# Initialiser l'interpréteur de commande
shell = Shell()

# Fonction pour gérer l'entrée de commandes
def handle_enter(event=None):
    user_input = entry.get().strip()
    entry.delete(0, tk.END)
    try:
        response = shell.onecmd(user_input)
        if response:
            text_zone.insert("end", f"> {user_input}\n{response}\n")
    except Exception as e:
        text_zone.insert("end", f"Erreur : {e}\n")
    text_zone.see("end")
    

# Associer l'événement "Entrée" à la fonction handle_enter pour la zone d'entrée
entry.bind("<Return>", handle_enter)

root.configure(bg="#333333")
text_zone.configure(font=("Courier", 12), bg="black", fg="lightgreen", padx=10, pady=10)
entry.configure(font=("Courier", 12), bg="#222222", fg="white")

# Lancer la boucle principale
root.mainloop()
