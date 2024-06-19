
import customtkinter as ctk
from library_manager import LibraryManager
from tkinter import filedialog
from datetime import datetime

class LibraryApp(ctk.CTk):
    """
    Classe pour l'interface graphique (GUI) de gestion de la bibliothèque.
    Utilise CustomTkinter pour créer une application graphique.
    """
    
    def __init__(self, library_manager):
        super().__init__()
        
        self.library_manager = library_manager
        
        self.title("Gestion de Bibliothèque")
        self.geometry("600x600")
        
        # Titre de l'application
        self.label = ctk.CTkLabel(self, text="Gestion de Bibliothèque", font=("Arial", 20))
        self.label.pack(pady=20)
        
        # Cadre pour ajouter des livres
        self.add_book_frame = ctk.CTkFrame(self)
        self.add_book_frame.pack(pady=10)
        
        # Entrée pour le titre du livre
        self.title_entry = ctk.CTkEntry(self.add_book_frame, placeholder_text="Titre")
        self.title_entry.pack(side="left", padx=5)
        
        # Entrée pour l'auteur du livre
        self.author_entry = ctk.CTkEntry(self.add_book_frame, placeholder_text="Auteur")
        self.author_entry.pack(side="left", padx=5)

        # Entrée pour la description du livre
        self.description_entry = ctk.CTkEntry(self.add_book_frame, placeholder_text="Description")
        self.description_entry.pack(side="left", padx=5)
        
        # Entrée pour la maison d'édition du livre
        self.publisher_entry = ctk.CTkEntry(self.add_book_frame, placeholder_text="Maison d'Edition")
        self.publisher_entry.pack(side="left", padx=5)
        
        # Entrée pour la date d'ajout du livre
        self.date_entry = ctk.CTkEntry(self.add_book_frame, placeholder_text="Date d'Ajout (YYYY-MM-DD)")
        self.date_entry.pack(side="left", padx=5)
        
        # Bouton pour ajouter une image
        self.image_button = ctk.CTkButton(self.add_book_frame, text="Ajouter Image", command=self.add_image)
        self.image_button.pack(side="left", padx=5)
        
        # Stockage du chemin de l'image
        self.image_path = None
        
        # Bouton pour ajouter un livre
        self.add_button = ctk.CTkButton(self.add_book_frame, text="Ajouter", command=self.add_book)
        self.add_button.pack(side="left", padx=5)
        
        # Textbox pour afficher la liste des livres
        self.books_textbox = ctk.CTkTextbox(self, state='disabled', wrap='none')
        self.books_textbox.pack(pady=20, fill="both", expand=True)
        
        self.refresh_books()
        
    def add_image(self):
        """
        Ouvre une boîte de dialogue pour sélectionner une image.
        """
        self.image_path = filedialog.askopenfilename(title="Sélectionner une image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        
    def add_book(self):
        """
        Ajoute un livre à la collection à partir des entrées utilisateur.
        """
        title = self.title_entry.get()
        author = self.author_entry.get()
        description = self.description_entry.get()
        publisher = self.publisher_entry.get()
        date_added = self.date_entry.get()
        image = self.image_path
        
        if title and author:
            self.library_manager.add_book(title, author, description, publisher, date_added, image)
            self.refresh_books()
            self.title_entry.delete(0, 'end')
            self.author_entry.delete(0, 'end')
            self.description_entry.delete(0, 'end')
            self.publisher_entry.delete(0, 'end')
            self.date_entry.delete(0, 'end')
            self.image_path = None
        
    def refresh_books(self):
        """
        Rafraîchit la liste des livres affichés dans la textbox.
        """
        self.books_textbox.configure(state='normal')
        self.books_textbox.delete('1.0', 'end')
        books = self.library_manager.get_books()
        for book in books:
            self.books_textbox.insert('end', f"Titre: {book['title']} Auteur: {book['author']}Description: {book['description']} Maison d'Edition: {book['publisher']} Date d'Ajout: {book['date_added']} Image: {book['image']}")
        self.books_textbox.configure(state='disabled')

if __name__ == "__main__":
    library_manager = LibraryManager()
    app = LibraryApp(library_manager)
    app.mainloop()
