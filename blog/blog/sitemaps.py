from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site

from board.models import Board


class BoardSitemap(Sitemap):
    changefreq = ("weekly",)
    priority = 0.9

    # your domain name
    def get_urls(self, site=None, **kwargs):
        site = Site(domain="yourdomain.com", name="yourdomain.com")
        return super(BoardSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return Board.objects.all()

    def lastmod(self, obj):
        return obj.update_date