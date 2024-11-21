from rest_framework.routers import DefaultRouter
from .views import (
    ExploitationViewSet,
    SalarieViewSet,
    OperationCulturaleViewSet,
    OperationPhytosanitaireViewSet
)

router = DefaultRouter()
router.register(r'exploitations', ExploitationViewSet)
router.register(r'salaries', SalarieViewSet)
router.register(r'operations-culturales', OperationCulturaleViewSet)
router.register(r'operations-phytosanitaires', OperationPhytosanitaireViewSet)

urlpatterns = router.urls
