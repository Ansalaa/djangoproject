from django.db import models

class Book(models.Model):      #Database model definition
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    price=models.IntegerField()
    pages=models.IntegerField()
    cover=models.ImageField(upload_to="images")
    pdf=models.FileField(upload_to="pdf")
