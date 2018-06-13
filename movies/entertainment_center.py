import fresh_tomatoes
import media

inside_out = media.Movie("Inside Out",
                         "A story of human's emotions",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

# print(insideo_ut.poster_image_url)


about_time = media.Movie("About Time",
                         "A man who can travel through time",
                         "http://t2.gstatic.com/images?q=tbn:ANd9GcRfwt52UbEpXfHM_tl69MNpqOQwAoVZrA2KY02pJSve0BUvyOr2",
                         "https://www.youtube.com/watch?v=T7A810duHvw")

# print(about_time.storyline)

queen = media.Movie("Queen",
                    "A woman gains new-found independence",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcRrt1YcpBelyLKnadqLZOHrcFuq_Lt12qEmPshRXKszw3eYWOV8",
                    "https://www.youtube.com/watch?v=KGC6vl3lzf0")

# print(queen.storyline)

# queen.show_trailer()

coco = media.Movie("Coco", "A boy's family history",
                   "http://t3.gstatic.com/images?q=tbn:ANd9GcS3FGIsangc2iauB89mttkiBAvIDj_O952Ypk2p5QqABby--L6d",
                   "https://www.youtube.com/watch?v=Rvr68u6k5sI")

if_only = media.Movie("If only",
                      "If you had one day more with the girl of your dreams",
                      "http://www.gstatic.com/tv/thumb/movieposters/160181/p160181_p_v8_ae.jpg",
                      "https://www.youtube.com/watch?v=3z5XDNHmBco")

breakfast_at_tiffany = media.Movie("Breakfast at Tiffany's",
                                   "A young woman who lives in NYC",
                                   "http://t2.gstatic.com/images?q=tbn:ANd9GcSAvX7uUNQ-aLJeLshTakwSAHeGlVPgmqXEnGSb06h-ctGb6Ud1",
                                   "https://www.youtube.com/watch?v=-XcLVQCDtbM")

movies = [inside_out, about_time, queen, coco, if_only, breakfast_at_tiffany]

fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.valid_ratings)

print(media.Movie.__doc__)
