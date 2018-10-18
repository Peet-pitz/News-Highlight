from flask import render_template
from . import main
from ..requests import get_news
from ..models import Source, Article


# Review = reviews.Review

# views
@main.route('/')
def index() :
    sources = get_news()
    print(sources)
    
    title = 'Home - welcome '
    return render_template('index.html', title=title, sources=sources)




# @main.route('/news/<int:id>')
# def news(
#     '''
#     View news page function that returns the news details page and its data
#     '''
#     news= get_news(id)
#     title = 'news'
   

#     return render_template('news.html', title=title, news=news)

