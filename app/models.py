class Source:
    """
    Movie class to define movie object
    """

    def __init__(self, id, name):

        self.id = id
        self.name = name
          


class Article:
    all_articles = []

    def __init__(self, author, title, description, urlToImage, publishedAt, content):
        self.movie_id = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    

  
