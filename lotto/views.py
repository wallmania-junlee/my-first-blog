from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Hello Mysite!</h1>')

from .models import GuessNumbers
from .forms import PostForm

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, "lotto/default.html", {"lottos" : lottos})
    #return HttpResponse('<h1>Hello Mysite!</h1>')
    # browser의 request를 받아서 template("lotto/default.html")에 전달한다는 의미
    # 추가적으로 object 보내줄 수 있는데 {} -> 아무것도 안보내주겠다는 의미

def post(request):
    if request.method == "POST":
        # save data
        # return HttpResponse("POST method")
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            #return HttpResponse("Saved OK")
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {"form" : form})


# 모든 url에 대하여 lotto/form.html로 render 하게 되어 있다.
# 우리가 원하는 건
# 1) 게시 : lotto/form.html로 render
# 2) Post method : save data & redirect to main page

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto" : lotto})
