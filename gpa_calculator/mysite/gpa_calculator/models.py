from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class Schedule(models.Model):
    user = models.OneToOneField('User')

    def __unicode__(self):
        return 'Schedule for ' + self.user.name

class Course(models.Model):
    GRADE_CHOICES = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('D-', 'D-'),
        ('F+', 'F+'),
        ('F', 'F'))

    course_name = models.CharField(max_length=40)
#    schedule = models.ManyToManyField('Schedule', related_name='course')
    units = models.FloatField()
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)


    # grade_to_gradeValue = {'A+': 4.0, 
    #                         'A': 4.0, 
    #                         'A-': 3.7, 
    #                         'B+': 3.3,
    #                         'B': 3.0,
    #                         'B-': 2.7,
    #                         'C+': 2.3,
    #                         'C': 2.0,
    #                         'C-': 1.7,
    #                         'D+': 1.3,
    #                         'D': 1.0,
    #                         'D-': 0.7,
    #                         'F+': 0.3,
    #                         'F': 0.0 }


    def __unicode__(self):
        return self.course_name