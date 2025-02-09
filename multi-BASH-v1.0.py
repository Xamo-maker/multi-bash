import tkinter as tk
import webbrowser
import time
import cmd
import urllib.request
import random
import os
import subprocess
import sys
import shutil
import platform
import psutil
from datetime import datetime, timedelta

# variable au lancement
launch_time = time.asctime()

# Classe de commandes
class Shell(cmd.Cmd):
    prompt = ""  # Pas de prompt car géré par l'interface Tkinter
    
    def do_help(self, arg, ):
        #Affiche la liste des commandes disponibles
        return('''Commandes disponibles: checkCPU, monitorCPU, rollDice, openurl [url], exit, clear, checkDiskSpace, detailPC, currentTime, launchTime, pipInstall [package], calc (calcul), creatorGitHub, openGitHub [profil] [reposit], helpPython, helpVsCode, helpNotepad, genPassword, helpSublimeText, creator, uptime''')

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
        try:
            webbrowser.open(url)
            return("Ouvrir le lien : {url}")
        except Exception as e:
            return("Erreur lors de l'ouverture du lien : {e}")

    def do_openGitHub(self ,line, profil, repos):
        if profil == "" and repos == "":
            return("mettre openGitHub [profil] [roposit]\n"
                   "openGitHub bash\n"
                   "bashGitHub\n")
        elif profil == "bash" and repos == "":
            webbrowser.open("https://github.com/Xamo-maker/multi-bash")
            return "ouverture du github..."
        else:
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

    def do_creator(self, arg):
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

    def do_checkDiskSpace(self, arg):
        """Vérifie l'espace disque disponible."""
        try:
            # Vérifie l'espace disque sur le chemin actuel ou spécifié
            path = arg if arg else "."
            usage = shutil.disk_usage(path)
            
            # Formatage des données
            total = usage.total / (1024 ** 3)  # Convertir en Go
            used = usage.used / (1024 ** 3)
            free = usage.free / (1024 ** 3)
            
            return (
                f"Informations sur le disque pour le chemin '{path}':\n"
                f"  - Total : {total:.2f} Go\n"
                f"  - Utilisé : {used:.2f} Go\n"
                f"  - Libre : {free:.2f} Go"
            )
        except FileNotFoundError:
            return f"Chemin '{arg}' introuvable."
        except Exception as e:
            return f"Une erreur s'est produite : {e}"

    def do_detailPC(self, arg):
        """
        Affiche les informations du système : CPU et RAM.
        """
        try:
            # Informations sur le processeur
            cpu = platform.processor()
            if not cpu:  # Pour les systèmes où `platform.processor()` ne retourne rien
                cpu = platform.uname().machine
            
            # Informations sur la RAM
            if os.name == "posix":  # Pour Linux/macOS
                with open('/proc/meminfo', 'r') as meminfo:
                    lines = meminfo.readlines()
                    mem_total = next((line for line in lines if "MemTotal" in line), None)
                    if mem_total:
                        mem_total = int(mem_total.split()[1]) // 1024  # Convertir en Mo
            elif os.name == "nt":  # Pour Windows
                import ctypes
                kernel32 = ctypes.windll.kernel32
                memory_status = ctypes.c_ulonglong()
                kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(memory_status))
                mem_total = memory_status.value // 1024  # Convertir en Mo
            else:
                mem_total = "Inconnu"
            
            return f"Processeur : {cpu}\nRAM : {mem_total} Mo"
        except Exception as e:
            return f"Erreur lors de la récupération des informations système : {e}"

    def do_monitorCPU(self, arg):
        #Surveille l'utilisation du CPU en temps réel.
        return "Surveillance de l'utilisation du CPU. Appuyez sur Ctrl+C pour quitter."
        try:
            while True:
                cpu_usage = psutil.cpu_percent(interval=1)  # Calcule l'utilisation toutes les secondes
                return f"Utilisation du CPU : {cpu_usage}%"
        except KeyboardInterrupt:
            return "\nSurveillance arrêtée."
            return "Surveillance CPU terminée."

    def do_checkCPU(self, arg):
        """Affiche un aperçu de l'état actuel du CPU."""
        try:
            # Utilisation globale du CPU
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Fréquence du CPU
            cpu_freq = psutil.cpu_freq()
            current_freq = cpu_freq.current if cpu_freq else "Inconnu"
            min_freq = cpu_freq.min if cpu_freq else "Inconnu"
            max_freq = cpu_freq.max if cpu_freq else "Inconnu"
            
            # Nombre de cœurs
            logical_cores = psutil.cpu_count(logical=True)
            physical_cores = psutil.cpu_count(logical=False)

            # Résultat à afficher
            return (
                f"Utilisation globale du CPU : {cpu_usage}%\n"
                f"Fréquence actuelle : {current_freq:.2f} MHz\n"
                f"Fréquence minimale : {min_freq:.2f} MHz\n"
                f"Fréquence maximale : {max_freq:.2f} MHz\n"
                f"Cœurs logiques : {logical_cores}\n"
                f"Cœurs physiques : {physical_cores}"
            )
        except Exception as e:
            return f"Une erreur s'est produite lors de la vérification du CPU : {e}"

    def do_bashGitHub(self, arg):
        webbrowser.open("https://github.com/Xamo-maker/multi-bash")
        return "ouverture du GitHub..."

    def do_creatorGitHub(self, arg):
        webbrowser.open("https://github.com/Xamo-maker")
        return "ouverture du GitHub du createur Xamo-Maker..."

    def do_rollDice(self, arg):
        roll = random.randint(1, 6)
        return f"{roll}"

    def do_systemInfo(self, arg):
        """Affiche les informations sur le système."""
        try:
            # Informations sur le système d'exploitation
            os_name = platform.system()
            os_version = platform.version()
            os_release = platform.release()
            architecture = platform.architecture()[0]

            # Informations sur le processeur
            cpu = platform.processor()
            cores_physical = psutil.cpu_count(logical=False)
            cores_logical = psutil.cpu_count(logical=True)

            # Informations sur la mémoire
            memory = psutil.virtual_memory()
            total_memory = memory.total / (1024 ** 3)  # Convertir en Go

            # Construire la sortie
            result = (
                f"=== Informations Système ===\n"
                f"Système d'exploitation : {os_name} {os_release}\n"
                f"Version : {os_version}\n"
                f"Architecture : {architecture}\n"
                f"\n"
                f"=== Informations CPU ===\n"
                f"Processeur : {cpu}\n"
                f"Cœurs physiques : {cores_physical}\n"
                f"Cœurs logiques : {cores_logical}\n"
                f"\n"
                f"=== Informations Mémoire ===\n"
                f"Mémoire totale : {total_memory:.2f} Go\n"
            )
            return result
        except Exception as e:
            return f"Une erreur s'est produite lors de la récupération des informations système : {e}"

    def do_uptime(self, arg):
        """Affiche depuis combien de temps le système est en fonctionnement."""
        try:
            # Temps de démarrage du système
            boot_time_timestamp = psutil.boot_time()
            boot_time = datetime.fromtimestamp(boot_time_timestamp)

            # Temps actuel
            now = datetime.now()

            # Calcul de la durée écoulée
            uptime_duration = now - boot_time

            # Formatage de la durée
            days = uptime_duration.days
            hours, remainder = divmod(uptime_duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Construire la sortie
            result = (
                f"=== Uptime Système ===\n"
                f"Le système a démarré le : {boot_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Durée de fonctionnement : {days} jours, {hours} heures, {minutes} minutes, {seconds} secondes\n"
            )
            return result
        except Exception as e:
            return f"Une erreur s'est produite lors du calcul du uptime : {e}"

    def default(self):
        #Commande par défaut pour les entrées non reconnues
        return("Commande inconnue ou syntaxe incorrecte.")


# Interface graphique
root = tk.Tk()
root.title("multi-bash v0.9")

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
            text_zone.insert("end", f">>> {user_input}\n{response}\n")
    except Exception as e:
        text_zone.insert("end", f"Erreur : {e}\n")
    text_zone.see("end")
    

# Associer l'événement "Entrée" à la fonction handle_enter pour la zone d'entrée
entry.bind("<Return>", handle_enter)

root.configure(bg="#333333")
text_zone.configure(font=("Courier", 12), bg="black", fg="lightgreen", padx=10, pady=10)
entry.configure(font=("Courier", 12), bg="#222222", fg="white")

return("logiciel sous license MIT, github:https://github.com/Xamo-maker/multi-bash")

# Lancer la boucle principale
root.mainloop()
