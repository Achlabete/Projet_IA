import os
import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def create_or_replace_folder(user_name):
    """
    Crée un dossier pour l'utilisateur ou avertit si une vidéo existe déjà.

    :param user_name: Nom de l'utilisateur.
    :return: Chemin du dossier de l'utilisateur.
    """
    base_path = "users"
    user_path = os.path.join(base_path, user_name)
    
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    if os.path.exists(user_path):
        response = messagebox.askyesno("Vidéo existante", f"Une vidéo pour {user_name} existe déjà. Voulez-vous la remplacer ?")
        if not response:
            return None  # Annuler si l'utilisateur ne veut pas remplacer
    else:
        os.makedirs(user_path)
    
    return user_path

def record_video(user_folder):
    """
    Capture une vidéo en demandant à l'utilisateur de se positionner.

    :param user_folder: Chemin du dossier de l'utilisateur.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Erreur", "Impossible d'accéder à la caméra.")
        return
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_path = os.path.join(user_folder, "video_test.mp4")
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    instructions = [
        "Regardez la caméra de face.",
        "Tournez-vous de profil gauche (après avoir appuyer sur OK).",
        "Tournez-vous de profil droit (après avoir appuyer sur OK)."
    ]
    
    frame_count = 0
    total_frames = 50  # Environ 2.5 secondes à 20 FPS pour chaque position
    
    for instruction in instructions:
        messagebox.showinfo("Instruction", instruction)
        while frame_count < total_frames:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Erreur", "Erreur lors de la capture vidéo.")
                cap.release()
                out.release()
                return
            
            cv2.imshow("Capture Vidéo", frame)
            out.write(frame)
            frame_count += 1
            
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Quitter en appuyant sur 'q'
                break

        frame_count = 0  # Réinitialiser pour la prochaine instruction

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Succès", f"Vidéo enregistrée dans {output_path}.")

def main_interface():
    """
    Interface principale pour demander le nom de l'utilisateur.
    """
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale

    user_name = simpledialog.askstring("Nom", "Entrez votre nom :")
    if not user_name:
        messagebox.showwarning("Nom requis", "Vous devez entrer un nom.")
        return

    user_folder = create_or_replace_folder(user_name)
    if user_folder:
        record_video(user_folder)
    # print(user_folder)
    return user_name
if __name__ == "__main_interface__":
    main_interface()
