# from app import app
import urllib.request,json

# import json
from .models import Source
from .models import Article

import ssl
ssl._create_default_https_context = ssl._create_unverified_context



# getting api key
api_key = None

# getting the news based url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    """
    function that gets the json response to our url request
    """
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url :
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response["sources"]:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results


# def get_newss(id):
#     get_news_details_url = base_url.format(id, api_key)

#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(news_details_data)

#         news_object = None
#         if news_details_response:
#             id = news_details_response.get('id')
#             name = news_details_response.get('name')
#             urlToImage = news_details_response.get('urlToImage')
           

#             news_object = Source(id, name,urlToImage)

#     return news_object


def process_results(news_list):

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
              
        news_object = Source(id, name,description,url,category)
        news_results.append(news_object)

    return news_results





