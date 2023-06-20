from django.shortcuts import render
from .test_data_creation import create_authors, create_publishers, create_libraries, create_books, create_users, create_reviews

def create_authors(request):
    create_authors()
    return render(request, 'message.html', {'message': 'Authors created!'})

def create_publishers(request):
    create_publishers()
    return render(request, 'message.html', {'message': 'Publishers created!'})

def create_libraries(request):
    create_libraries()
    return render(request, 'message.html', {'message': 'Libraries created!'})

def create_books(request):
    create_books()
    return render(request, 'message.html', {'message': 'Books created!'})

def create_users(request):
    create_users()
    return render(request, 'message.html', {'message': 'Users created!'})

def create_reviews(request):
    create_reviews()
    return render(request, 'message.html', {'message': 'Reviews created!'})
