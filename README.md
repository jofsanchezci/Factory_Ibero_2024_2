# Patrón de Diseño Factory

## Descripción

El **Patrón Factory** es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una clase padre, 
permitiendo a las subclases alterar el tipo de objetos que se crearán. En lugar de instanciar directamente las clases, el patrón 
Factory delega la responsabilidad de la creación de objetos a subclases o métodos que permiten una mayor flexibilidad y modularidad.

## ¿Cuándo usar el Patrón Factory?

El patrón Factory es útil cuando:
- La lógica de creación de objetos es compleja o puede cambiar en el futuro.
- Deseas que el código sea más modular y fácil de extender.
- Hay múltiples tipos de objetos relacionados que se necesitan crear y sus diferencias no afectan a la interfaz pública del cliente.

## Beneficios del Patrón Factory
1. **Desacoplamiento**: Separa el proceso de creación de objetos de la lógica principal de la aplicación.
2. **Flexibilidad**: Permite agregar nuevos tipos de objetos sin modificar el código existente.
3. **Reutilización**: Centraliza la creación de objetos, lo que reduce la duplicación de código.
4. **Mantenimiento**: Facilita el mantenimiento al reducir el impacto de los cambios en la creación de objetos.

## Ejemplo

En este ejemplo, implementamos un sistema de gestión de inventarios de una biblioteca utilizando el patrón Factory. 
La fábrica (`BookFactory`) crea diferentes tipos de libros (ficción, no ficción y ciencia), y el sistema de inventario 
gestiona los libros creados.

```python
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
```

## Ejecución del Sistema

El sistema puede ejecutar las siguientes funcionalidades:
- **Añadir un libro**: Utiliza la fábrica `BookFactory` para crear libros de ficción, no ficción o ciencia.
- **Eliminar un libro**: Se elimina del inventario un libro dado su ISBN.
- **Buscar libro por título**: Busca un libro en el inventario basado en su título.
- **Mostrar inventario**: Muestra todos los libros actualmente disponibles en la biblioteca.

## Ventajas del Uso del Patrón Factory en este Sistema

1. **Extensibilidad**: Puedes añadir nuevos tipos de libros fácilmente al sistema sin modificar la lógica de inventario.
2. **Modularidad**: El proceso de creación de objetos está desacoplado de la lógica de gestión de inventarios.
3. **Flexibilidad**: Cambios en la creación de libros (por ejemplo, añadiendo campos nuevos) solo afectarán a la fábrica, no al resto del código.

# Bloc Medium

https://medium.com/all-you-need-is-clean-code/patrones-de-dise%C3%B1o-b7a99b8525e