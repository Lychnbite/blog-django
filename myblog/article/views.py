import article
from django.core.checks import messages
from django.shortcuts import redirect, render,HttpResponse, get_object_or_404
from .forms import ArticleForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.





def index(request):
    context = {
        "number":10,
        "number1":20
    }
    return render(request,"article/index.html",context)




def about(request):

    return render(request,"article/about.html")




@login_required(login_url="user:login")
def dashboard(request):
    keyword = request.GET.get("keyword")
    if keyword:

        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"article/dashboard.html",{"articles":articles})


    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"article/dashboard.html",context)




@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False) 

        article.author = request.user
        article.save()
        return redirect("article:index")



    return render(request,"article/addarticle.html", {"form":form})



def detail(request,id):

    article = get_object_or_404(Article,id=id)

    comments = article.comments.all()
    return render(request,"article/detail1.html", {"article":article, "comments":comments})



@login_required(login_url="user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance=article)
    
    
    if form.is_valid():

        article = form.save(commit=False) 

        article.author = request.user
        article.save()
        return redirect("article:dashboard")
    
    return render(request,"article/update.html", {"form":form})



@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()

    return redirect("article:dashboard")



def addComment(request,id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":

        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author= comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))

    