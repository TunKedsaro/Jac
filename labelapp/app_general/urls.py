from django.urls import path,include
from app_general import views

urlpatterns = [
    path("",views.index,name='home'),
    path('about',views.about),
    path('form',views.form,name="form"),
    path('edit/<person_id>',views.edit,name='edit'),
    path('delete/<id_remove>',views.delete,name='delete')
]

# from django.urls import path,include
# from app_general import views

# urlpatterns = [
#     path("",views.index,name="index"),
#     path("upload/",views.upload_image,name='upload_image')
# ]