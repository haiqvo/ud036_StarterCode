import fresh_tomatoes
from media import Movie

# @author Hai Vo


# Wonder women instance
wonder_woman_movie = Movie("Wonder Woman",
                           "DC Wonder Woman moive",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt"
                           "-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",
                           "https://www.youtube.com/watch?v=5lGoQhFb4NM")

# guardian of the Galaxy instance
gofg = Movie("Guardians of the Galaxy Vol. 2",
             "Guardians of the Galaxy",
             "http://t2.gstatic.com/images?q=tbn:ANd9GcSzRHzPW9j56dGLliO"
             "dUV0lzjeUwfALe9Zn2Ys7Kkwj4YsvDpsh",
             "https://www.youtube.com/watch?v=2cv2ueYnKjg")

# your name instance
your_name = Movie("Your Name",
                  "Japanese animated film",
                  "http://t0.gstatic.com/images?q=tbn:ANd9GcR7gFSo85sz"
                  "XEdjrPsBO992eUhkX0qwALaQWdCj-BOfcaU0kpH-",
                  "https://www.youtube.com/watch?v=s0wTdCQoc2k")

# pirates of the Caribbean instance
poc = Movie("Pirates of the Caribbean: Dead Men Tell No Tales",
            "Pirates of the Caribbean",
            "http://t2.gstatic.com/images?q=tbn:ANd9GcRRynPaJp56dmpf"
            "UGeG3x9o7WirlscR99wbxw56RX3qtMOf-KEn",
            "https://www.youtube.com/watch?v=a5V5C8mEVzY")

# list of movies objects
movies = [wonder_woman_movie, gofg, your_name, poc]

# called to create html file and display movie trailer page.
fresh_tomatoes.open_movies_page(movies)
