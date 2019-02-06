from django.contrib import admin
from django.urls import path, re_path
from conf.views import add_room, rooms, edit_room, delete_room, room_details, reservation, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new', add_room, name='new'),
    path('', rooms, name='rooms'),
    path('room/<id>', room_details, name='details'),
    path('room/edit/<id>', edit_room, name='edit'),
    path('room/delete/<id>', delete_room, name='delete'),
    path('reservation/<id>', reservation, name='reservation'),
    path('search', search, name='search'),
]
