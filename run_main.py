import subprocess
import threading

def run_demo():
    """
    Lance demo.py dans un processus séparé.
    """
    print("Lancement du mode validation (demo.py)... Appuyez sur Enter pour interrompre.")
    process = subprocess.Popen(["python", "demo.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    return process

def wait_for_interrupt(process):
    """
    Attend que l'utilisateur presse Enter pour interrompre demo.py.
    """
    input(">> ")  # Attend que l'utilisateur presse Enter.
    print("Interruption demandée. Arrêt de demo.py...")
    process.terminate()  # Arrête le processus demo.py.
    process.wait()  # Attend la fin complète du processus.
    print("Mode validation interrompu.")

def run_training():
    """
    Lance main.py pour l'entraînement.
    """
    print("Lancement du mode entraînement (main.py)...")
    subprocess.run(["python", "main.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("Entraînement terminé.")

def main_loop():
    """
    Boucle principale alternant entre validation et entraînement.
    """
    while True:
        # Lancer demo.py
        demo_process = run_demo()

        # Attendre interruption (Enter pressé)
        wait_for_interrupt(demo_process)

        # Lancer main.py pour l'entraînement
        run_training()

        # Retour au mode validation
        print("Retour au mode validation...\n")

if __name__ == "__main__":
    main_loop()
