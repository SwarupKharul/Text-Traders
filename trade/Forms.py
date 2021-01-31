from django.forms import ModelForm
from .models import Books


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['bookname', 'author', 'description','condition','image1','image2','image3','image4','contact','city']
