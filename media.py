
# @author Hai Vo


class Movie(object):
    """ Movie class contains a title, short summary, image, and trailer
    constructor:
        title (String)
        storyline (String)
        poster_image_url (url)
        trailer_youtube_url (url)

    title is the name of the Movie
    storyline is the summary (not use yet)
    poster_image_url is the url to images
    trailer_youtube_url is the url to the trailer
    """
    def __init__(self,
                 title,
                 storyline,
                 poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
