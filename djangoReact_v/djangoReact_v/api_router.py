from rest_framework import routers

from djangoReact_v.mainapps.api.viewsets import CarViewSet, MaintenanceViewSet, ComplaintsViewSet, GuideViewSet
router = routers.DefaultRouter()

router.register('Cars', CarViewSet)
router.register('Maintenances', MaintenanceViewSet)
router.register('Complaints', ComplaintsViewSet)
router.register('Guides', GuideViewSet)
