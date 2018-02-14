from django.shortcuts import render
import datetime
from django.http import HttpResponseBadRequest
# Create your views here.
import json

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
	if request.method == 'GET':
		return render(request,'html/index.html')
	elif request.method == 'POST':
		if request.POST.get('name'):
			name = request.POST.get('name')
			if name != None:
				date = datetime.datetime.now().strftime("%y-%m-%d")
				grids = {"grid":[" "," "," "," "," "," "," "," "," "]}
				return render(request,'html/play.html',{'name':name,'date':date,'grids':json.dumps(grids)})
	return render(request,'html/index.html')
