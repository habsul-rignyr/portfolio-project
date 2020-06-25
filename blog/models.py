from django.db import models

# Create a blog model

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

#title
#pub_date
#body
#image




# Add the Blog app to the settings


# Create a migration


# Migrate


# Add to admin