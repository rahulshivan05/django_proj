from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatar', default='avatar.png')
	background = models.ImageField(upload_to='backgrounds', default='background.jpg')
	following = models.ManyToManyField(User, related_name='following', blank=True)
	bio = models.TextField(default='no bio....')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)

	def get_my_posts(self):
		return self.post_set.all()

	@property
	def num_posts(self):
		return self.post_set.all().count()

	def get_following(self):
		return self.following.all()

	def get_following_users(self):
		following_list = [p for p in self.get_following()]
		return following_list

