from django.db import models
import uuid

# Create your models here.
CONTRIBUTER_TYPES = (
    ("Trainer", "Trainer"),
    ("Judge", "Judge"),
    ("Mentor", "Mentor")
)
class Team(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=128)
    image = models.CharField(null=True, blank=True,max_length=100)
    def __str__(self):
        return f"{self.name}, {self.token}"

class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discord_id = models.CharField(max_length=100, null=True)
    discord_username = models.CharField(max_length=100, null=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)
    study_at = models.CharField(blank=True, null=True, max_length=100)
    excitement = models.IntegerField()
    experience = models.CharField(max_length=100)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id}, {self.fullname} , {self.email} ->Team:  {self.team}"

class Contributor(models.Model):    
    name = models.CharField(max_length=70, blank=False, default='')
    type = models.CharField(max_length=70,choices=CONTRIBUTER_TYPES, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    picture = models.ImageField(null=True, blank=True,upload_to='images/contributors')
    facebook_url = models.CharField(max_length=255, null=True, blank=True, default='')
    instagram_url = models.CharField(max_length=255, null=True, blank=True, default='')
    linkedin_url = models.CharField(max_length=255, null=True, blank=True, default='')
    twitter_url = models.CharField(max_length=255, null=True, blank=True, default='')
    
    def __str__(self):
        return str(self.name)