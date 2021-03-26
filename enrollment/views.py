from django.views.generic import DetailView

from . import models


class SubjectDetailView(DetailView):
    model = models.Subject
