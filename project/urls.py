from rest_framework import routers
from .api import ProjectViewset

router=routers.DefaultRouter()

router.register('api/project', ProjectViewset, 'project')

urlpatterns = router.urls

