from django.db import models

# student model defined here
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
