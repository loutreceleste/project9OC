from django.contrib import admin
from reviews.models import CreateReviewWithTicket

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'rating', 'time_created', 'user')

admin.site.register(CreateReviewWithTicket, ReviewAdmin)
