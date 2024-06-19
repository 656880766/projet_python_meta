import sys
from library_manager import LibraryManager
from interfaces.terminal_interface import TerminalInterface
from interfaces.gui_interface import LibraryApp
import customtkinter as ctk

class MainApp:
    """
    Classe principale pour démarrer l'application de gestion de bibliothèque.
    Permet de choisir entre une interface terminale et une interface graphique.
    """
    
    def __init__(self):
        self.data_file = "data.json"
        self.library_manager = LibraryManager(self.data_file)

    def choose_interface(self):
        """
        Affiche le menu pour choisir l'interface utilisateur.
        
        Returns:
            str: Le choix de l'utilisateur.
        """
        print("Choisissez une interface:")
        print("1. Interface Terminal")
        print("2. Interface Graphique (GUI)")
        choice = input("Choix: ")
        return choice

    def run(self):
        """
        Exécute l'interface choisie par l'utilisateur.
        """
        choice = self.choose_interface()
        match choice:
            case '1':
                TerminalInterface(self.library_manager).run()
            case '2':
                ctk.set_appearance_mode("System")
                ctk.set_default_color_theme("blue")
                app = LibraryApp(self.library_manager)
                app.mainloop()
            case _:
                print("Choix invalide. Veuillez relancer le programme et choisir 1 ou 2.")

if __name__ == "__main__":
    MainApp().run()
