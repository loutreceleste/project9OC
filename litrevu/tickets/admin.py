from django.contrib import admin
from tickets.models import CreateTicket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'date_created', 'user')

admin.site.register(CreateTicket, TicketAdmin)
