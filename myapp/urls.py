from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns = [
    path('views1/',views.views1,name="views1"),
    path('views2/<email>',views.views2,name="views2"),
    path('views3/<name>',views.views3,name="views3"),
]
