from django.contrib import admin
from .models import submission,programmingLanguage,submissionDetails,verdict
# Register your models here.

admin.site.register(
    [
        submission,
        programmingLanguage,
        submissionDetails,
        verdict
    ]
)