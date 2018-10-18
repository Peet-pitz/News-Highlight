from flask import render_template
from . import main
from ..requests import get_news
from ..models import Source, Article


# Review = reviews.Review

# views

# @main.route('/')
# def index() :
#     sources = get_news()
#     print(sources)
    
#     title = 'Home - welcome '
#     return render_template('index.html', title=title, sources=sources)






