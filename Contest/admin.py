from django.contrib import admin
from .models import leaderboard, contest

admin.site.register(
    [
        leaderboard, contest
    ]
)