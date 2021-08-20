
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse


# Create your views here.

def index(request):
    return render(request, "frontpage/index.html")

def login(request):
    if request.method == 'POST':
        nome = request.POST["nome"]
        email = request.POST['email']
        senha1 = request.POST["senha1"]
        senha2 = request.POST["senha2"]

        if senha1 != senha2:
            return HttpResponseRedirect(reverse("notfound", args=('notfound',)))

        return render(request, "frontpage/index.html", {
            'nome':nome,
            'email':email,
            'senha':senha1
        })

        #if title == "" or senha1 == "":
        #    return HttpResponseRedirect(reverse("new_post"))
        #else:
        #    new_post = Posts(title=title, post=post)
        #    new_post.save()
        #    
    return render(request, "frontpage/login.html")

def notfound(request, not_found):
    return render(request, "frontpage/notfound.html")