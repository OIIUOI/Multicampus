from random import sample
import re
from django.shortcuts import render
import random

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


def calculate(request, a, b):
    add_ab = int(a) + int(b)
    sub_ab = int(a) - int(b)
    mul_ab = int(a) * int(b)
    div_ab = int(a) / int(b)
    content = {
        "add": add_ab,
        "sub": sub_ab,
        "mul": mul_ab,
        "div": div_ab,
        "a": a,
        "b": b,
    }
    return render(request, "calculate.html", content)


def js(request):
    return render(request, "js.html")


def jsresult(request):
    js_list = [
        "별것없었음",
        "개죽음",
        "척많이 지고 살았네염",
        "성격 개더러웠네염",
        "평범하게 살다 갔네염",
        "으 진짜 별로..",
        "맛있는 건 많이 먹었네염",
        "오 갓생러",
        "오 재능러",
        "살리에르",
        "먹고 산 게 기적임",
        "홧병",
        "하고싶은 건 다했네염",
        "성깔대로 살았네염",
    ]

    js = random.choice(js_list)
    name = request.GET.get("name")
    content = {"js": js, "name": name}
    return render(request, "jsresult.html", content)


def loreminput(request):
    return render(request, "loreminput.html")


def loremoutput(request):
    words = ["아아아아아", "이이이이이", "오오오오오", "에에에에에", "이이이이이"]
    block = int(request.GET.get(block))
    word = int(request.GET.get(word))
    for _ in range(block):
        random.sample(words,word)
        <br>