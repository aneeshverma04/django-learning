from django.db import models

# this is a table that inherits from models.Model
class Post(models.Model):
	# these are columns... own data types
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title