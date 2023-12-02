from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    
class Prompt(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat' , on_delete=models.CASCADE)
    prompt = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.prompt
    
class Response(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat' , on_delete=models.CASCADE)
    prompt = models.ForeignKey('Prompt' , on_delete=models.CASCADE)
    response = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.response


    
class Settings(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    temperature = models.IntegerField(default=0)
    optionA = models.CharField(max_length=1000)
    optionB = models.CharField(max_length=1000)
    max_documents = models.IntegerField(default=0)
    number_of_sections = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    
class File(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    chat = models.ForeignKey('Chat' , on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.name
    
class Chat(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, default='Untitled')
    # option field having 3 choices named Option A, Option B, Upload 
    option_selected = models.CharField(choices=(('A', 'Option A'), ('B', 'Option B'), ('C', 'Upload')), max_length=1, default='A')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title