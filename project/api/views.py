from django.http import HttpResponse, HttpResponseForbidden
from .assets import assets
from django.core.handlers.wsgi import WSGIRequest
import json

from django.views import View
# Create your views here.

class BaseView(View):
    def post(self, req):
        return HttpResponse("Use a GET request. ")

class UserView(BaseView):
    def get(self, req, username):
        body = assets.getuserbody(username)
        x = assets.sendrequser(body)
        data = json.loads(x.text)
        return HttpResponse(str(data))

class BoardView(BaseView):
    def get(self, req, boardname):
        body = assets.getboardbody(boardname)
        x = assets.sendreqboard(body)
        data = json.loads(x.text)
        return HttpResponse(str(data))