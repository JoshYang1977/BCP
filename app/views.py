from django.shortcuts import render, HttpResponse
from .models import scenario, department, bcp_measure
import random
# Create your views here.



def frontpage(request):
    readcolor_from_outside = random.randint(1,5)
    sces = scenario.objects.get(id=readcolor_from_outside)
    measures_one = bcp_measure.objects.get(color_id=readcolor_from_outside, name_id=1)
    deps_one = department.objects.get(id=1)
    measures_two = bcp_measure.objects.get(color_id=readcolor_from_outside, name_id=2)
    deps_two = department.objects.get(id=2)
    return render(request,'app/index.html',{'sces':sces, 'measures_one':measures_one,
                                            'deps_one':deps_one, 'measures_two':measures_two,
                                                                                    'deps_two':deps_two})
