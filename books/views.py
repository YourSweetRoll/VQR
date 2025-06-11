from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Chapter
from .forms import BookForm, ChapterForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def chapter_detail(request, book_id, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id, book_id=book_id)
    chapters = Chapter.objects.filter(book_id=book_id).order_by('id')
    chapter_list = list(chapters)
    current_index = chapter_list.index(chapter)

    next_chapter = chapter_list[current_index + 1] if current_index < len(chapter_list) - 1 else None
    previous_chapter = chapter_list[current_index - 1] if current_index > 0 else None

    return render(request, 'books/chapter_detail.html', {
        'chapter': chapter,
        'next_chapter': next_chapter,
        'previous_chapter': previous_chapter
    })

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

def create_chapter(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.book = book
            chapter.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ChapterForm()
    return render(request, 'books/create_chapter.html', {'form': form, 'book': book})