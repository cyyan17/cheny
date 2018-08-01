# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json
from home_application.models import Data

def compute(request):
    pr1 =int(request.GET.get('pr1'))
    pr2 =int(request.GET.get('pr2'))
    result = pr1 * pr2
    Data.objects.create(
          pr1=pr1,
          pr2=pr2,
          result=result,
        )
    return render_json({'result':result})


def home(request):
    """
    首页
    """
    all_record=Data.objects.all()
    ctx = {
          'all_record':all_record
    }
    return render_mako_context(request, '/home_application/home.html',ctx)

def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
