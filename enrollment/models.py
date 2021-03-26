from django.db import models
from django.urls import reverse


class Student(models.Model):
    id_no = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    subjects = models.ManyToManyField('enrollment.Subject', through='enrollment.StudentSubject')

    def __str__(self):
        return self.name


class Subject(models.Model):
    school_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    instructor = models.CharField(max_length=250)
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    units = models.DecimalField(max_digits=18, decimal_places=1)
    room = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    remarks = models.CharField(max_length=2000, blank=True, default='')
    students = models.ManyToManyField(Student, through='enrollment.StudentSubject')

    def __str__(self):
        return f'{self.code} - {self.title}'

    def get_absolute_url(self):
        return reverse('subject-detail', args=[self.pk])


class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} / {self.subject}'
