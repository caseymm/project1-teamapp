from django.db import models

# Create your models here.

class Basketball(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.CharField(max_length=5000)
    number = models.CharField(unique=True, max_length=3)
    position = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=3)
    year = models.CharField(max_length=15)
    hometown = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    about = models.CharField(max_length=5000)
    personal = models.CharField(max_length=5000)
    
    def __unicode__(self):
        return U'%s %s' %(self.number, self.name, self.image)

    
    class Meta(object):
        verbose_name_plural = "Basketball"
        #ordering = ('-date','name',)
    
    #def __unicode__(self):
        #return U'%s | %s' %(self.number, self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(player, self).save(*args, **kwargs)

class Football(models.Model):
    name = models.CharField(unique=True, max_length=100)
    
    class Meta(object):
        verbose_name_plural = "Football"

class Baseball(models.Model):
    name = models.CharField(unique=True, max_length=100)
    
    class Meta(object):
        verbose_name_plural = "Baseball"
    
    
