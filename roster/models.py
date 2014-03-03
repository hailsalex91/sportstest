from django.db import models

# Create your models here.
class statistics(models.Model):
    pid = models.IntegerField(unique=True, max_length=9)
    firstName = models.CharField(unique=False, max_length=50)
    lastName = models.CharField(unique=False, max_length=50)
    tournaments = models.IntegerField(unique=False, max_length=10)
    rounds = models.IntegerField(unique=False, max_length=10)
    rounds_completed = models.IntegerField(unique=False, max_length=10)
    completion_pct = models.IntegerField(unique=False, max_length=10)
    par = models.IntegerField(unique=False, max_length=10)
    below_par = models.IntegerField(unique=False, max_length=10)
    sixties = models.IntegerField(unique=False, max_length=10)
    low = models.IntegerField(unique=False, max_length=10)
    high = models.IntegerField(unique=False, max_length=10)
    strokes = models.IntegerField(unique=False, max_length=10)
    average = models.IntegerField(unique=False, max_length=10)

class sports(models.Model):
    name = models.CharField(unique=False, max_length=50)
    gender = models.CharField(unique=False, max_length=50)
    url = models.TextField(unique=False)
    roster_url = models.TextField(unique=False)

class athlete(models.Model):
    pid = models.IntegerField(unique=True, max_length=9)
    firstName = models.CharField(unique=False, max_length=50)
    lastName = models.CharField(unique=False, max_length=50)
    gradYear = models.CharField(unique=False, max_length=50)
    age = models.IntegerField(unique=False, max_length=9)
    height = models.CharField(unique=False, max_length=50)
    favorite_food = models.CharField(unique=False, max_length=50)
    details = models.TextField(unique=False)
    athlete_image = models.CharField(unique=False, max_length=200)
    school_id = models.IntegerField(unique=False, max_length=9)
    school_name = models.CharField(unique=False, max_length=200)
    school_city = models.CharField(unique=False, max_length=50)
    school_state = models.CharField(unique=False, max_length=50)
    school_country = models.CharField(unique=False, max_length=50)
    school_url = models.CharField(unique=False, max_length=200)
    twitter_handle = models.CharField(unique=False, max_length=50)
    twitter_widgetID = models.CharField(unique=False, max_length=50)

    class meta(object):
        verbose_name_plural = "Athletes"
        ordering = ('pid','firstName','lastName')
    def __unicode__(self):
        return U'%s %s' %(self.firstName, self.pid)
class school(models.Model):
    school_id = models.IntegerField(unique=True, max_length=9)
    name = models.CharField(unique=False, max_length=50)
    city = models.CharField(unique=False, max_length=50)
    state = models.CharField(unique=False, max_length=50)
    country = models.CharField(unique=False, max_length=50)
    athlete = models.ManyToManyField(athlete)

    class meta(object):
        ordering = ('school_id','name')
    def __unicode__(self):
        return U'%s %s' %(self.school_id, self.name)
class coach(models.Model):
    pid = models.IntegerField(unique=True, max_length=9)
    firstName = models.CharField(unique=False, max_length=50)
    lastName = models.CharField(unique=False, max_length=50)
    title = models.CharField(unique=False, max_length=50)
    isActive = models.BooleanField()
    athlete_image = models.CharField(unique=False, max_length=200)
    details = models.TextField(unique=False)

    class meta(object):
        verbose_name_plural = "Coaches"
        ordering = ('pid','name')
    def __unicode__(self):
        return U'%s %s' %(self.firstName, self.pid)

class golfImage(models.Model):
    url_id = models.CharField(unique = False, max_length=200)

    class meta(object):
        ordering = ('url_id')
    def __unicode__(self):
        return U'%s' %(self.url_id)