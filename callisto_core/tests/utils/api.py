from callisto_core.notification.api import CallistoCoreNotificationApi
from callisto_core.reporting.api import CallistoCoreMatchingApi

from django.contrib.sites.models import Site


class SiteAwareNotificationApi(CallistoCoreNotificationApi):

    def user_site_id(self, user):
        Site.objects.filter(id=1).update(domain='testserver')
        return 1


class SendDisabledNotificationApi(SiteAwareNotificationApi):

    def send(self):
        pass


class CustomMatchingApi(CallistoCoreMatchingApi):

    def process_new_matches(*args):
        pass