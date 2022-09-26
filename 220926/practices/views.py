from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def isodd(request, num):
    if num == 0:
        answer = "0"
    elif num % 2 == 1:
        answer = "홀수"
    else:
        answer = "짝수"
    content = {"odd": answer, "num": num}
    return render(request, "isodd.html", content)
