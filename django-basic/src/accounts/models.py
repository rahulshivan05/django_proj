from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', null=True, upload_to='profile')
	bio = models.CharField(max_length=5000, default='No Bio...')
	phone_no = models.CharField(max_length=13)
	age = models.CharField(max_length=12)

	def __str__(self):
		return f'{self.user.username} Profile'

	# def save(self, new_image=False, *args, **kwargs):
	# 	if new_image:
	# 		small=rescale_image(self.image, width=300, height=300)
	# 		self.image_scale = SimpleUploadedFile(name, small_pic)
	# 	super(Profile, self).save(*args, **kwargs)

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
