from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("register", views.register, name="register"),
    path("new_drink", views.new_drink, name="new_drink"),
    path("edit_drink/<int:drink_id>/", views.edit_drink, name="edit_drink"),
    path("like/<int:drink_id>/", views.like, name="like"),
    path("unlike/<int:drink_id>/", views.unlike, name="unlike")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)