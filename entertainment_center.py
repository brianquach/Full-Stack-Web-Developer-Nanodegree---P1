"""
Copyright 2015 Brian Quach
Licensed under MIT (https://github.com/brianquach/Full-Stack-Web-Developer-Nanodegree---P1/blob/master/LICENSE)  # noqa
"""
import fresh_tomatoes
import media


def get_movie_list():
    """Fetches a list of movie objects.

    Returns:
        A list of movie objects; each movie object represents one of my
        favorite movies with relevant movie data.
    """
    shawshank = media.Movie("Shawshank Redemption",
        "Two imprisoned men bond over a number of years, finding solace and " +
        "eventual redemption through acts of common decency.",
        1994,
        "142 min",
        "R",
        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
        "https://www.youtube.com/watch?v=NmzuHjWmXOc")

    batman = media.Movie("Batman: Mask of the Phantasm",
        "Batman is wrongly implicated in a series of murders of mob bosses " +
        "actually done by a new vigilante assassin.",
        1993,
        "76 min",
        "PG",
        "http://www.gstatic.com/tv/thumb/movieposters/15294/p15294_p_v7_ab.jpg",  # noqa
        "https://www.youtube.com/watch?v=G__jUFD4Ef8")

    toy_story_2 = media.Movie("Toy Story 2",
        "When Woody is stolen by a toy collector, Buzz and his friends vow " +
        " to rescue him, but Woody finds the idea of immortality in a " +
        "museum tempting.",
        1999,
        "92 min",
        "G",
        "http://www.gstatic.com/tv/thumb/movieposters/24266/p24266_p_v7_ab.jpg",  # noqa
        "https://www.youtube.com/watch?v=Lu0sotERXhI")

    spirited_away = media.Movie(
    	"Spirited Away",
        "During her family's move to the suburbs, a sullen 10-year-old girl " +
        "wanders into a world ruled by gods, witches, and spirits, and " +
        "where humans are changed into beasts.",
        2001,
        "125 min",
        "PG",
        "http://www.gstatic.com/tv/thumb/dvdboxart/29914/p29914_d_v7_aa.jpg",
        "https://www.youtube.com/watch?v=ByXuk9QqQkk")

    goodfellas = media.Movie(
        "Goodfellas",
        "Henry Hill and his friends work their way up through the mob " +
        "hierarchy.",
        1990,
        "146 min",
        "R",
        "http://t0.gstatic.com/images?q=tbn:ANd9GcSkuxYKBhyPQq4e_cbYRDfZRjWkUx2GIKlUpUkHiuVeLg2GhN0D",  # noqa
        "https://www.youtube.com/watch?v=2ilzidi_J8Q")

    conjuring = media.Movie(
        "The Conjuring",
        "Paranormal investigators Ed and Lorraine Warren work to help a " +
        "family terrorized by a dark presence in their farmhouse.",
        2013,
        "112 min",
        "R",
        "http://t2.gstatic.com/images?q=tbn:ANd9GcQnHDbJFDDZYC5g9gHa6-NqBE8JUet_iRIPXJym8CtaHsVQa76M",  # noqa
        "https://www.youtube.com/watch?v=k10ETZ41q5o")

    rush_hour_2 = media.Movie(
        "Rush Hour 2",
        "Carter and Lee head to Hong Kong for vacation, but become " +
        "embroiled in a counterfeit money scam.",
        2001,
        "90 min",
        "PG-13",
        "http://www.gstatic.com/tv/thumb/dvdboxart/28145/p28145_d_v7_aa.jpg",
        "https://www.youtube.com/watch?v=SCTzYY95Aw4")

    indie_gamer = media.Movie(
        "Indie Game: The Movie",
        "The Movie is the first feature documentary film about making video " +
        "games. It looks specifically at the underdogs of the video game " +
        "industry, indie game developers, who sacrifice money, health and " +
        "sanity to realize their lifelong dreams of sharing their visions " +
        "with the world.",
        2012,
        "94 min",
        "Not Rated",
        "https://upload.wikimedia.org/wikipedia/en/f/fc/Indie_Game_The_Movie_poster.png",  # noqa
        "https://www.youtube.com/watch?v=dINgx0y4GqM")

    goonies = media.Movie(
        "The Goonies",
        "In order to save their home from foreclosure, a group of misfits " +
        "set out to find a pirate's ancient treasure.",
        1985,
        "114 min",
        "PG",
        "http://ia.media-imdb.com/images/M/MV5BMTY1Mzk3MTg0M15BMl5BanBnXkFtZTcwOTQzODYyMQ@@._V1_SX640_SY720_.jpg",  # noqa
        "https://www.youtube.com/watch?v=hJ2j4oWdQtU")

    return [
        shawshank, batman, toy_story_2, spirited_away, goodfellas,
        conjuring, rush_hour_2, indie_gamer, goonies
    ]

print(fresh_tomatoes.open_movies_page(get_movie_list()))
