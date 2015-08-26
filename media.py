import webbrowser

class Movie():
	def __init__(self, move_title, storyline, release_year, movie_length, poster_image, trailer_youtube):
		self.title = move_title
		self.storyline = storyline
		self.release_year = release_year
		self.movie_length = movie_length
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)