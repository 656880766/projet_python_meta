from library_manager import LibraryManager

class TerminalInterface:
    """
    Classe pour l'interface terminal de gestion de la bibliothèque.
    Permet à l'utilisateur d'ajouter, de supprimer et de lister des livres via le terminal.
    """
    
    def __init__(self, library_manager):
        self.library_manager = library_manager

    def run(self):
        """
        Lance l'interface terminale et affiche le menu principal.
        """
        while True:
            self.show_menu()
            choice = input("Choisissez une option: ")
            self.handle_choice(choice)

    def show_menu(self):
        """
        Affiche le menu principal.
        """
        print("\nMenu:")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Lister les livres")
        print("4. Quitter")

    def handle_choice(self, choice):
        """
        Traite le choix de l'utilisateur.
        
        Args:
            choice (str): Le choix de l'utilisateur.
        """
        match choice:
            case '1':
                self.add_book()
            case '2':
                self.remove_book()
            case '3':
                self.list_books()
            case '4':
                exit()
            case _:
                print("Choix invalide. Veuillez réessayer.")

    def add_book(self):
        """
        Demande à l'utilisateur d'entrer le titre et l'auteur du livre à ajouter.
        """
        title = input("Titre du livre: ")
        author = input("Auteur du livre: ")
        self.library_manager.add_book(title, author)
        print("Livre ajouté avec succès.")

    def remove_book(self):
        """
        Demande à l'utilisateur d'entrer le titre du livre à supprimer.
        """
        title = input("Titre du livre à supprimer: ")
        self.library_manager.remove_book(title)
        print("Livre supprimé avec succès.")

    def list_books(self):
        """
        Affiche la liste des livres de la collection.
        """
        books = self.library_manager.list_books()
        if books:
            print("\nListe des livres:")
            for book in books:
                print(f"Titre: {book['title']}, Auteur: {book['author']}")
        else:
            print("Aucun livre trouvé.")
