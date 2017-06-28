
# @author Hai Vo

class Movie(object):
    """ Movie class contains a title, short summary, image, and trailer """
    def __init__(self, title, storyline, poster_image_url,trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
