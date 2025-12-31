from django.db import models

# Create your models here.
class courses(models.Model):
    # Remove this line completely OR
    id = models.AutoField(primary_key=True)

    course_name = models.CharField(max_length=100, default="General")
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name  # product ka n ame return karta he


class signup_v(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class mycours(models.Model):
    # Remove this line completely OR
    user = models.ForeignKey(signup_v, on_delete=models.CASCADE)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.course_name  # product ka n ame return karta he



