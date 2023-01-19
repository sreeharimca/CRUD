from django.urls import path
from .views import *
urlpatterns=[
# path('load_form/',load_form),
# path('add/',add),
# path('show/',show),
# path('edit/<int:id>',edit),
# path('delete/<int:id>',delete),
#
# path('update/<int:id>',update),
#
#     path("load/",bload),
#     path('badd/',badd),
#      path('bshow/',bshow),
#     path('bdelete/<int:id>',bdelete),
#      path('bedit/<int:id>',bedit),
#     path('bupdate/<int:id>', bupdate),


path('a/',a),

path('register/',register),
path('login/',login),
    path('newindex/',newindex),

path('cload/',cload),
    path('cadd/',cadd),
    path('cshow/', cshow),
    path('cedit/<int:id>',cedit),
    path('cdelete/<int:id>', cdelete),

]