import certifi
import urllib3
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework import status
from revproxy.views import ProxyView
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def redirect_handler(request):
    if request.method == 'GET':
        # return Response("", status=status.)
        resp = HttpResponseRedirect("http://localhost:4200")
        # request.session['test'] = 'icle'
        resp.set_cookie('test', "redirect", max_age=3, expires=2,
                        domain="localhost", secure=False, httponly=True)

        return resp


class TestProxyView(ProxyView):
    upstream = 'http://example.com'

    def __init__(self, *args, **kwargs):
        super(ProxyView, self).__init__(*args, **kwargs)
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
