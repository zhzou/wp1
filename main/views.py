from django.shortcuts import render
import datetime
from django.http import HttpResponseBadRequest
# Create your views here.
import json

def index(request):
	if request.method == 'GET':
		return render(request,'index.html')
	elif request.method == 'POST':
		if request.POST.get('username'):
			name = request.POST.get('username')
			if name != None:
				date = datetime.datetime.now().strftime("%y-%m-%d")
				grids = {"grid":[" "," "," "," "," "," "," "," "," "],"winner":" "}
				return render(request,'play.html',{'name':name,'date':date,'grids':json.dumps(grids)})
	return HttpResponseBadRequest()