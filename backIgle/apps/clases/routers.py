from rest_framework.routers import DefaultRouter
from .viesets import ClasesVieset

router = DefaultRouter()

router.register(r'clases', ClasesVieset)

urlpatterns = router.urls