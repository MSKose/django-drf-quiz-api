'''
namespace makes sure app names doesn't collide with, say third party default names. 
see: https://docs.djangoproject.com/en/4.1/topics/http/urls/#reversing-namespaced-urls
also: https://stackoverflow.com/a/48058661
'''


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls', namespace='quiz')),
]
