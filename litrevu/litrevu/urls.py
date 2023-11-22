from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

admin.autodiscover()

from tickets import views as ticket_views
from authentication import views as authentication_views
from reviews import views as reviews_views


urlpatterns = [
        path('admin/', admin.site.urls),

        path('', authentication_views.connection, name='login'),
        path('logout/', authentication_views.logout_user, name='logout'),
        path('inscription/', authentication_views.signup_page, name='inscription'),
        path('follow/', authentication_views.follow_view, name='follow'),

        path('flux/', ticket_views.flux, name='flux'),
        path('my_flux/', ticket_views.my_flux, name='my_flux'),
        path('ticket/', ticket_views.ticket, name='ticket'),
        path('ticket/<int:id>/change/', ticket_views.edit_ticket, name='edit_ticket'),
        path('ticket/<int:id>/delete/', ticket_views.delete_ticket, name='delete_ticket'),

        path('review_whithout_ticket/', reviews_views.review_whithout_ticket, name='review_whithout_ticket'),
        path('review_whith_ticket/<int:id>/', reviews_views.review_whith_ticket, name='review_whith_ticket'),
        path('edit_review/', reviews_views.edit_review, name='edit_review'),
        path('review/<int:id>/change/', reviews_views.edit_review, name='edit_review'),
        path('review/<int:id>/delete/', reviews_views.delete_review, name='delete_review'),


    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
