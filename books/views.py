from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from books.models import Book


# Create your views here.
def render_book_catalogue(request, user_id):
    template = 'books/catalogue.html'
    context = {
        'catalogue': Book.objects.filter(owner_id=user_id),
        'user': user_id # 1. Pass user id in order to create books automatically assigned to our user.
    }
    return render(request, template, context)


def render_create_book_form(request, user_id):
    template = 'books/create_book_form.html'
    context = {
        'user': user_id
    }
    return render(request, template, context)


def process_create_book_form(request):
    if request.method == 'POST':
        new_book = Book(
            name=request.POST['name'],
            author=request.POST['author'],
            genre=request.POST['genre'],
            language=request.POST['language'],
            publication_date=request.POST['publication_date'],
            owner_id=request.POST['owner_id'],
        )
        new_book.save()

        return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_id': new_book.owner.id}))
    return HttpResponse('Error: method not allowed.')


def render_edit_book_form(request, book_id):
    template = 'books/edit_book_form.html'
    context = {
        'book': Book.objects.get(id=book_id) # 1. Get the book we're updating.
    }
    return render(request, template, context)


def process_edit_book_form(request, book_id):
    if request.method == 'POST':
        updated_book = Book.objects.get(id=book_id) # 1. Retrieve the book we're updating.
        updated_book.name = request.POST['name'] # 2. Update its attributes.
        updated_book.author = request.POST['author']
        updated_book.genre = request.POST['genre']
        updated_book.language = request.POST['language']
        updated_book.publication_date=request.POST['publication_date']
        updated_book.save() # 3. Save the updated book instance.

        return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_id': updated_book.owner.id}))
    return HttpResponse('Error: method not allowed.')


def delete_book(request, book_id):
    deleted_book = Book.objects.get(id=book_id)
    deleted_book.delete()

    return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_id': deleted_book.owner.id}))