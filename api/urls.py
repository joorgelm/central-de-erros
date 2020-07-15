from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('user', UserViewSet)
router.register('agent', AgentViewSet)
