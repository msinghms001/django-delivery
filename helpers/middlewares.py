from datetime import time
from django.utils import timezone
from backports.zoneinfo import ZoneInfo

class Tmz():

    def __init__(self,resp):
        self.resp=resp

    def __call__(self, req):
        tznamee=ZoneInfo('Asia/Kolkata')
        # print('passing through!',tznamee)
        # timezone.activate(tznamee)
        return self.resp(req)