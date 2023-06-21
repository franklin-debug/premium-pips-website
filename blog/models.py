from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/')
	description = models.CharField(max_length=250)
	date = models.DateField()

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('blog_detail',kwargs={
			'blog_id':self.id
		})