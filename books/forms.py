from django import forms
from .models import Book
from .models import Chapter

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'description']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content']