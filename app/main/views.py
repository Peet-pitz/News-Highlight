from flask import render_template
from . import main
from ..requests import get_news, get_news
from ..models import Source, Article


# Review = reviews.Review

# views
@main.route('/')
def index() :
    sources = get_news('general')
    print(sources)
    # bbc_sport = get_news('bbc_sport')
    # buzz_feed = get_news('buzz_feed')
    title = 'Home - welcome '
    return render_template('index.html', title=title, sources=sources)

# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html', movies=searched_movies)


@main.route('/news/<int:id>')
def news(id):
    '''
    View news page function that returns the news details page and its data
    '''
    news= get_news(id)
    title = 'news'
   

    return render_template('news.html', title=title, news=news)

# @main.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
# def new_review(id) :
#     form = ReviewForm()
#     movie = get_movie(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.title.data
#         new_review = Review(movie.id,title, movie.poster,review)
#         new_review.save_review()
#         return redirect(url_for('.movie', id = movie.id))
#     title = f'{movie.title} review'
#     return render_template('new_review.html', title = title, review_form = form, movie = movie)
