from django import forms
from django.forms import fields
from .models import Article




# Oluşturulan Article Modeli ile bağlantı sağlanıyor bu form sınıfı sayesinde
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # form modeli ile bağlantı kurulan yer
        fields = ["title","content","article_image"]



