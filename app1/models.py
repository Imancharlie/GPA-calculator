from django.db import models

# # Create your models here.
# class Credit(models.Model):

class Credit(models.Model):
    credit=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True ,blank=True)
    #participants=
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.credit
    
    
class Electrical(models.Model):
    coarse=models.CharField(max_length=200)
    credit=models.IntegerField()
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse

class Civil(models.Model):
    coarse=models.CharField(max_length=200)
    credit=models.IntegerField()
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse

class Mechanical(models.Model):
    coarse=models.CharField(max_length=200)
    credit=models.CharField(max_length=200,null=True ,blank=True)
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse

class Mechanic(models.Model):
    coarse=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True ,blank=True)
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse

class Metallugy(models.Model):
    coarse=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True ,blank=True)
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse

class Quantity(models.Model):
    coarse=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True ,blank=True)
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse
    

class Industrial(models.Model):
    coarse=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True ,blank=True)
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse

class Textile(models.Model):
    coarse=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True ,blank=True)
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse

class Chemical(models.Model):
    coarse=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True ,blank=True)
    updated=models.DateTimeField( auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.coarse
    
