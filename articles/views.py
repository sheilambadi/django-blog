from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')

    #3rd param is dictionary with data to send to html
    return render(request, 'articles/article_list.html', {'articles': articles})
