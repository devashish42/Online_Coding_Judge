from django.contrib import admin
from .models import testCase, problem

admin.site.register(
    [
        testCase, problem
    ]
)