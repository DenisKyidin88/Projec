from rest_framework import routers

from djangoReact_v.mainapps.api.viewsets import CarViewSet, MaintenanceViewSet, ComplaintsViewSet, GuideViewSet

router = routers.DefaultRouter()

router.register('car', CarViewSet)
router.register('maintenance', MaintenanceViewSet)
router.register('complaints', ComplaintsViewSet)
router.register('guide', GuideViewSet)
