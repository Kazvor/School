
from ckeditor_uploader.fields import RichTextUploadingField



from django.db import models

class Predmet(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
class Teacher(models.Model):
    name_teacher=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='photo/')
    predmet=models.ManyToManyField(Predmet )
    def __str__(self) :
        return self.name_teacher
        

class Words_of_the_day(models.Model):
    title=models.CharField(max_length=255, verbose_name='Загаловка')
    description=RichTextUploadingField(verbose_name='Описание')
    greetings_title=models.CharField(max_length=100)
    greetings_description=models.CharField(max_length=250)

    def __str__(self) :
        return self.title

# class Classes(models.Model):
#     class_name=models.CharField(max_length=12)

# class Students(models.Model):
#     full_name=models.CharField(max_length=100)
#     class_name=models.ForeignKey(Classes,on_delete=models.CASCADE)

# class Magazine(models.Model):
#     CHOISE=(
#         (5,5),
#         (4,4),
#         (3,3),
#         (2,2),
#     )
#     students=models.ForeignKey(Students,on_delete=models.CASCADE)
#     marks=models.CharField(max_length=10,choices=CHOISE)
class Slaider(models.Model):
    title=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='photo/')

    



