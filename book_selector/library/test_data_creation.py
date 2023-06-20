from .models import Author, Publisher, Library, Book, User, Review

def create_authors():
    author_names = ['Stephen King', 'J.K. Rowling', 'George R.R. Martin', 'Neil Gaiman', 'Margaret Atwood']
    for name in author_names:
        Author.objects.create(name=name, email=name.lower().replace(' ', '') + '@example.com')

def create_publishers():
    publisher_names = ['Penguin Random House', 'Simon & Schuster', 'Hachette Livre', 'HarperCollins']
    for name in publisher_names:
        Publisher.objects.create(name=name, address=name.replace(' ', '') + ' St. New York, NY')

def create_libraries():
    library_names = ['New York Public Library', 'Brooklyn Public Library', 'Boston Public Library', 'Los Angeles Public Library']
    for name in library_names:
        Library.objects.create(name=name, address=name.replace(' ', '') + ' St. New York, NY')

def create_books():
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    libraries = Library.objects.all()

    Book.objects.create(
        title='The Shining',
        author=authors[0],
        publisher=publishers[0],
    )
    Book.objects.create(
        title='The Stand',
        author=authors[0],
        publisher=publishers[0],
        library=libraries[0],
    )
    Book.objects.create(
        title='Harry Potter and the Philosopher\'s Stone',
        author=authors[1],
        publisher=publishers[0],
    )
    Book.objects.create(
        title='Harry Potter and the Chamber of Secrets',
        author=authors[1],
        publisher=publishers[0],
    )
    Book.objects.create(
        title='A Game of Thrones',
        author=authors[2],
        publisher=publishers[1],
    )
    Book.objects.create(
        title='A Clash of Kings',
        author=authors[2],
        publisher=publishers[1],
        library=libraries[1],
    )

def create_users():
    user_names = ['John', 'Jane', 'Mary', 'Bob']
    for name in user_names:
        User.objects.create(name=name, email=name.lower() + '@example.com')

def create_reviews():
    books = Book.objects.all()
    users = User.objects.all()

    Review.objects.create(
        book=books[0],
        user=users[0],
        rating=4,
        comment='Great book!'
    )
    Review.objects.create(
        book=books[2],
        user=users[1],
        rating=5,
        comment='Loved it!'
    )