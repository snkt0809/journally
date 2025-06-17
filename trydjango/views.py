from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random


def home_view(request, *args, **kwargs):
    # random_id = random.randint(1, 4)
    # obj = Article.objects.get(id=random_id)
    article_qs = Article.objects.all()

    context = {
        "obj_list": article_qs,
        # "title": obj.title,
        # "content": obj.content,
    }

    HTML_STRING = render_to_string("home-view.html", context = context)
    # HTML_STRING = f"""
    # <h1>Welcome to Django! Have fun Sanket!</h1>
    # <br>
    # <h2>Article Title: {obj.title}</h2>
    # <p>Article Content: {obj.content},
    # Article ID: {obj.id}</p>
    # """

    return HttpResponse(HTML_STRING)