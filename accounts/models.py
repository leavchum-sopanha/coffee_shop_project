from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class CoffeeMenu(models.Model):
   name = models.CharField(max_length=200, null=True) 
   price = models.CharField(max_length=200, null=True) 
   description = RichTextUploadingField(null=True)
   image = models.ImageField(upload_to="coffee-menu")
   date_created = models.DateTimeField(auto_now_add=True, null=True) 

   def short_description(self):
      return self.description[:50] + "..." if self.description and len(self.description) > 50 else self.description

   def __str__(self):
      return self.name


class CoffeeGallery(models.Model):
   name = models.CharField(max_length=200, null=True) 
   image = models.ImageField(upload_to="coffee-gallery")
   date_created = models.DateTimeField(auto_now_add=True, null=True) 

   def __str__(self):
      return self.name


class CoffeeBlog(models.Model):
   name = models.CharField(max_length=200, null=True) 
   image = models.ImageField(upload_to="blog-gallery")
   description = RichTextUploadingField(null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True) 

   def short_description(self):
      return self.description[:200] + "..." if self.description and len(self.description) > 200 else self.description

   def __str__(self):
      return self.name


class CoffeeBanner(models.Model):
   name = models.CharField(max_length=200, null=True) 
   description = RichTextUploadingField(null=True)
   date_created = models.DateTimeField(auto_now_add=True, null=True) 

   def short_description(self):
      return self.description[:200] + "..." if self.description and len(self.description) > 200 else self.description

   def __str__(self):
      return self.name


class CoffeeAbout(models.Model): 
   name = models.CharField(max_length=200, null=True) 
   description = RichTextUploadingField(null=True)
   video = models.FileField(upload_to="videos/")
   image = models.ImageField(upload_to="coffee-about")
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   
   def short_description(self):
      return self.description[:200] + "..." if self.description and len(self.description) > 200 else self.description

   def __str__(self):
      return self.name


class CoffeeTopMenu(models.Model):
    name = models.CharField(max_length=200, null=True)
    section_id = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def short_description(self):
        return self.description[:200] + "..." if self.description and len(self.description) > 200 else self.description

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='reviews/')  
    rating = models.PositiveSmallIntegerField()  
    review_text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
         return f"{self.name} ({self.rating}/5)"


class Footer(models.Model):
    about_text = models.TextField()
    newsletter_link = models.URLField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    dribbble_link = models.URLField()
    behance_link = models.URLField()

    def __str__(self):
        return "Footer Information"
    
class SocialMedia(models.Model):
    socialMediaName = models.CharField(max_length=200, null=True)
    socialMediaURL = models.CharField(max_length=200, null=True)
    socialMediaImage = models.ImageField(upload_to ='SocialImages')

    def str(self):
        return f'{self.socialMediaName}'
    