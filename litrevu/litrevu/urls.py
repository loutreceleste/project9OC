from django.contrib import admin
from django.urls import path
from tickets import views as ticket_views
from authentication import views as authentication_views
from reviews import views as reviews_views
from follows import views as follows_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', authentication_views.connection, name='login'),
    path('logout/', authentication_views.logout_user, name='logout'),
    path('inscription/', authentication_views.signup_page, name='inscription'),

    path('flux/', ticket_views.flux, name='flux'),
    path('my_flux/', ticket_views.my_flux, name='my_flux'),
    path('ticket/', ticket_views.ticket, name='ticket'),
    path('edit_ticket/', ticket_views.edit_ticket, name='edit_ticket'),


    path('edit_review/', reviews_views.edit_review, name='edit_review'),
    path('review_whithout_ticket/', reviews_views.review_whithout_ticket, name='review_whithout_ticket'),
    path('review_whith_ticket/', reviews_views.review_whith_ticket, name='review_whith_ticket'),

    path('follows/', follows_views.follows, name='follows'),
]
