"""
Copyright 2015 Brian Quach
Licensed under MIT (https://github.com/brianquach/Full-Stack-Web-Developer-Nanodegree---P1/blob/master/LICENSE)
"""
import webbrowser

class Movie():
	"""Represents a movie.

	Attributes:
		title: A string representing the movie title.
		storyline: A string representing a brief summary of the movie story.
		release_year: An integer representing the movie release year.
		length: A string representing the movie length in minutes.
		rated: A string representing the Motion Picture Association of America's (MPAA) film rating.
		poster_image_url: A string representing a web URL to the movie poster.
		trailer_youtube_url: A string representing a web URL to the movie trailer.
	"""
	
	def __init__(self, title, storyline, release_year, length, rated, poster_image, trailer_youtube):
		"""Inits Movie with title, storyline, release_year, length, rated, poster_image, trailer_youtube"""
		self.title = title
		self.storyline = storyline
		self.release_year = release_year
		self.length = length
		self.rated = rated
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""Opens browser window with the Movie's youtube trailer URL"""
		webbrowser.open(self.trailer_youtube_url)