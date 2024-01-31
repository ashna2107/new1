from django.db import models

# Create your models here.
class reguser(models.Model):
    name=models.CharField(max_length=20)
    username = models.CharField(max_length=20,unique=True)
    phone=models.CharField(max_length=14)
    email=models.CharField(max_length=20)
    password = models.EmailField(max_length=20)
    address=models.CharField(max_length=100)
    profile=models.FileField(null=True)
    def __str__(self):
        return self.name

class compdance(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=20,unique=True)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    license=models.FileField()
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    profile = models.FileField(null=True)
    def __str__(self):
        return self.name

class compmusic(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=20,unique=True)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    license=models.FileField()
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    profile=models.FileField(null=True)
    def __str__(self):
        return self.name


class project(models.Model):
    mname = models.ForeignKey(compmusic, on_delete=models.CASCADE,null=True)
    dname = models.ForeignKey(compdance, on_delete=models.CASCADE,null=True)
    category=models.CharField(max_length=20)
    projectimage=models.FileField(max_length=20)
    client=models.CharField(max_length=20)
    date=models.DateField()
    projectdetail=models.TextField()


class about(models.Model):
    mname = models.ForeignKey(compmusic, on_delete=models.CASCADE, null=True)
    dname = models.ForeignKey(compdance, on_delete=models.CASCADE, null=True)
    special=models.CharField(max_length=40,null=True)
    native=models.CharField(max_length=40)
    achievements=models.CharField(max_length=40,null=True)
    fprice=models.IntegerField(null=True)
    disc=models.TextField(null=True)
    experience=models.IntegerField()

class booking(models.Model):
    user=models.ForeignKey(reguser,on_delete=models.CASCADE,null=True)
    mname=models.ForeignKey(compmusic,on_delete=models.CASCADE,null=True)
    dname=models.ForeignKey(compdance,on_delete=models.CASCADE,null=True)
    date= models.DateField()
    bdate=models.DateField()
    price=models.IntegerField()
    dis=models.TextField()
    address=models.TextField()
    status=models.CharField(max_length=20)
    paid=models.CharField(max_length=10,default='Not Paid')


class Reviews(models.Model):
    user = models.ForeignKey(reguser, on_delete=models.CASCADE)
    review = models.TextField()
    def _str_(self):
        return self.review

class contactus(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    message=models.CharField(max_length=300)
    def __str__(self):
        return self.name


