from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from dk_webapp_api.settings import DEBUG
if DEBUG:
    from views import AccountViewSet
else:
    from apps.users.views import AccountViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'account', AccountViewSet, base_name='account')

# Connect the routes back to djangos routes
urlpatterns = [
    url(r'^', include(router.urls))
]