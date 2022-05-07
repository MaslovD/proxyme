import certifi
import urllib3
from revproxy.views import ProxyView


class TestProxyView(ProxyView):
    upstream = 'http://example.com'

    def __init__(self, *args, **kwargs):
        super(ProxyView, self).__init__(*args, **kwargs)
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())