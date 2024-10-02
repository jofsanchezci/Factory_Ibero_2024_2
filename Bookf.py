from abc import ABC, abstractmethod

# Clase abstracta para representar los libros
class Book(ABC):
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    @abstractmethod
    def create(self):
        pass

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"

# Clases concretas de tipos de libros
class FictionBook(Book):
    def create(self):
        return f"Ficción: {self.title}"

class NonFictionBook(Book):
    def create(self):
        return f"No ficción: {self.title}"

class ScienceBook(Book):
    def create(self):
        return f"Ciencia: {self.title}"

# Fábrica para crear libros
class BookFactory:
    def create_book(self, book_type, title, author, isbn, copies):
        if book_type == "fiction":
            return FictionBook(title, author, isbn, copies)
        elif book_type == "nonfiction":
            return NonFictionBook(title, author, isbn, copies)
        elif book_type == "science":
            return ScienceBook(title, author, isbn, copies)
        else:
            raise ValueError(f"Tipo de libro '{book_type}' no reconocido.")

# Clase de inventario de la biblioteca
class LibraryInventory:
    def __init__(self):
        self.inventory = {}

    def add_book(self, book):
        if book.isbn in self.inventory:
            self.inventory[book.isbn].copies += book.copies
        else:
            self.inventory[book.isbn] = book
        print(f"Libro '{book.title}' añadido al inventario.")

    def remove_book(self, isbn):
        if isbn in self.inventory:
            removed_book = self.inventory.pop(isbn)
            print(f"Libro '{removed_book.title}' eliminado del inventario.")
        else:
            print(f"El libro con ISBN {isbn} no está en el inventario.")

    def search_by_title(self, title):
        found_books = [book for book in self.inventory.values() if book.title.lower() == title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No se encontraron libros con el título '{title}'.")

    def display_inventory(self):
        if not self.inventory:
            print("El inventario está vacío.")
        else:
            print("Inventario actual de la biblioteca:")
            for book in self.inventory.values():
                print(book)

# Uso del sistema con el patrón Factory
if __name__ == "__main__":
    factory = BookFactory()
    library = LibraryInventory()

    # Crear libros usando el patrón Factory
    book1 = factory.create_book("fiction", "Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0", 5)
    book2 = factory.create_book("nonfiction", "Sapiens", "Yuval Noah Harari", "978-1-56619-909-4", 3)
    book3 = factory.create_book("science", "Breve historia del tiempo", "Stephen Hawking", "978-0-14-044913-6", 2)

    # Agregar libros al inventario
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Mostrar el inventario
    library.display_inventory()

    # Buscar un libro por título
    print("\nBuscar libro 'Cien años de soledad':")
    library.search_by_title("Cien años de soledad")

    # Eliminar un libro
    print("\nEliminar libro con ISBN 978-1-56619-909-4:")
    library.remove_book("978-1-56619-909-4")

    # Mostrar el inventario después de eliminar
    print("\nInventario después de eliminar:")
    library.display_inventory()
