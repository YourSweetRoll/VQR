from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Chapter
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def chapter_detail(request, book_id, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id, book_id=book_id)
    return render(request, 'books/chapter_detail.html', {'chapter': chapter})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})