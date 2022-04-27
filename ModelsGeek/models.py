from django.db import models
# we use this file to create delete models or tables in database

class Modeltry(models.Model):
    #fields of model
    title = models.CharField(max_length=50)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.title
    ''' makemigrations basically generates the SQL commands for preinstalled
    apps (which can be viewed in installed apps in settings.py) and your newly
    created app’s model which you add in installed apps'''
    #Python manage.py makemigrations    we have to give this command in command panel
    #after above cmd we have to tye another cmd
    #Python manage.py migrate
    ''' migrate executes those SQL commands in the database file. '''

    # class Meta:
    #     verbose_name = _("Model_try")
    #     verbose_name_plural = _("Model_trys")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Model_try_detail", kwargs={"pk": self.pk})
