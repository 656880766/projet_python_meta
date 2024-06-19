
import json
from datetime import datetime

class LibraryManager:
    """
    Classe pour gérer les opérations de la bibliothèque.
    """
    
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        self.load_data()
        
    def load_data(self):
        """
        Charge les données de la bibliothèque à partir d'un fichier JSON.
        """
        try:
            with open(self.data_file, 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []
            
    def save_data(self):
        """
        Sauvegarde les données de la bibliothèque dans un fichier JSON.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.books, file, indent=4)
            
    def add_book(self, title, author, description, publisher, date_added, image):
        """
        Ajoute un livre à la bibliothèque.
        """
        new_book = {
            'title': title,
            'author': author,
            'description': description,
            'publisher': publisher,
            'date_added': date_added,
            'image': image
        }
        self.books.append(new_book)
        self.save_data()
        
    def get_books(self):
        """
        Retourne la liste des livres de la bibliothèque.
        """
        return self.books
