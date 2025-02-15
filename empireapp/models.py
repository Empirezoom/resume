from django.db import models

# Create your models here.




class CompanyProfile(models.Model):
    c_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    carousel1 = models.ImageField(upload_to='carousel')
    carousel2 = models.ImageField(upload_to='carousel')


        
    def __str__(self):
            return self.c_name
    class Meta:
        db_table = 'CompanyProfile'
        managed = True
        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfile'

class About(models.Model):
    sur_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField( max_length=100)
    date_created = models.DateField( auto_now_add=True)
    zip_num = models.IntegerField()
    copyright_link = models.CharField(max_length=100)
    whatsapp_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    a_logo = models.ImageField(upload_to='logo')
    cv = models.FileField( upload_to='Cv')
    about_me = models.TextField(default='about me at the top')
    date_of_birth = models.DateField()

        
    def __str__(self):
            return self.first_name
    class Meta:
        db_table = 'About'
        managed = True
        verbose_name = 'About'
        verbose_name_plural = 'About'

class Certification(models.Model):
    duration = models.CharField(max_length=300)
    degree = models.CharField(max_length=300) 
    school = models.CharField( max_length=300)
    address= models.CharField(max_length=300)

        
    def __str__(self):
            return self.school
    class Meta:
        db_table = 'Certification'
        managed = True
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'



class Category(models.Model):
    type = models.CharField(max_length=300)
    icon = models.CharField(max_length=300) 
  

        
    def __str__(self):
            return self.type
    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Contact(models.Model):
    full_name = models.CharField(max_length=180)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=180)
    message = models.TextField()
    sent = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)
    not_read = models.BooleanField(default=True)
        
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'