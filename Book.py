class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"

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

# Uso del sistema de gestión de inventarios
if __name__ == "__main__":
    library = LibraryInventory()

    # Crear libros
    book1 = Book("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0", 5)
    book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes", "978-1-56619-909-4", 3)
    book3 = Book("El amor en los tiempos del cólera", "Gabriel García Márquez", "978-0-14-044913-6", 2)
    book4 = Book("El Señor de los Anillos", "Tolkien", "978-0-14-044913-999", 4)

    # Agregar libros al inventario
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

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
