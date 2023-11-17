from django.shortcuts import render

# Create your views here.


def second(request):
    return render(request,"second.html")

def third(request):
    return render(request,"third.html")
dict = {
    "details":(
    {"name":"abhi","address":"dmm","marks":60,"degree":"btech"},
    {"name":"bbhi","address":"dmm","marks":70,"degree":"btech"},
    {"name":"cbhi","address":"dmm","marks":50,"degree":"btech"},
    {"name":"dbhi","address":"dmm","marks":40,"degree":"btech"},
    {"name":"ebhi","address":"dmm","marks":30,"degree":"btech"},
)
}

def index(request):
    return render(request,"index.html",context=dict)
