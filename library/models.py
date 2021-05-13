from django.db import models

# Create your models here.
class subject(models.Model):
	subject_name = models.CharField(blank=True, null=True, max_length=100)
	pdf_link1 = models.CharField(max_length = 200)
	pdf_link2 = models.CharField(max_length = 200)
	pdf_link3 = models.CharField(max_length = 200)
	pdf_link4 = models.CharField(max_length = 200)
	pdf_link5 = models.CharField(max_length = 200)

	content1 = models.TextField()
	content2 = models.TextField()
	content3 = models.TextField()
	content4 = models.TextField()
	content5 = models.TextField()

	def __str__(self):
		return self.subject_name