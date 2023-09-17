from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from djapp.views import UserloginViewSet
from djapp.views import CandidatViewSet
from djapp.views import OffreViewSet
from djapp.views import CandidaturesViewSet
from djapp.views import EntreViewSet
from djapp.views import MessageViewSet
from djapp.views import ping
from djapp.views import ping1
from djapp.views import ping2
from .views import UploadViewSet
from djapp.views import HauptuserViewSet
from djapp.views import ArticleViewSet
from djapp.views import AvisViewSet

router=routers.DefaultRouter()
router.register(r'Userlogin',UserloginViewSet)
router.register(r'Candidat',CandidatViewSet) 
router.register(r'Offre',OffreViewSet)
router.register(r'Candidatures',CandidaturesViewSet) 
router.register(r'Entrelogin',EntreViewSet)
router.register(r'Message',MessageViewSet)
router.register(r'Hauptuser',HauptuserViewSet) 
router.register(r'Article',ArticleViewSet) 
router.register(r'Avis',AvisViewSet) 
router.register(r'upload', UploadViewSet, basename="upload")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping, name='ping'),
    path('ping1/', ping1, name='ping1'),
    path('ping2/', ping2, name='ping2'),
    

    path('', include(router.urls)),
    
]
