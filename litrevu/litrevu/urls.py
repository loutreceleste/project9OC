from django.contrib import admin
from django.urls import path
from litrevu.ticket import views as ticket_views
from litrevu.authentication import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', authentication_views.accueil),
    path('inscription/', authentication_views.inscription),
    path('flux/', ticket_views.flux),
    path('ticket/', ticket_views.ticket),
    path('critique_sans_ticket/', ticket_views.critique_sans_ticket),
    path('critique_avec_ticket/', ticket_views.critique_avec_ticket),
    path('posts/', ticket_views.posts),
    path('modifier_critique/', ticket_views.modifier_critique),
    path('modifier_ticket/', ticket_views.modifier_ticket),
]
