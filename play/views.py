from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json

@csrf_exempt
def index(request):
	if request.META.get('CONTENT_TYPE') == 'application/json':
		if request.method == 'POST':
			griddict = json.loads(request.body.decode('utf8'))
			
			new_griddict = processGrid(griddict)
			print(new_griddict)
			return HttpResponse(json.dumps(new_griddict),content_type="application/json")
	return HttpResponse("OK")

def processGrid(griddict):
	#print(checkWinner(griddict['grid']))
	griddict['winner'] = checkWinner(griddict['grid'])
	if griddict['winner'] == ' ':
			griddict['grid'][griddict['grid'].index(' ')] = 'O'
			griddict['winner'] = checkWinner(griddict['grid'])	
	return griddict


def checkWinner(gridlist):
	try:
		if checkPosition(gridlist,0,1,2) and gridlist[0] == 'O':
			return 'O'
		if checkPosition(gridlist,3,4,5) and gridlist[3] == 'O':
			return 'O'
		if checkPosition(gridlist,6,7,8) and gridlist[6] == 'O':
			return 'O'
		if checkPosition(gridlist,0,3,6) and gridlist[0] == 'O':
			return 'O'
		if checkPosition(gridlist,1,4,7) and gridlist[1] == 'O':
			return 'O'
		if checkPosition(gridlist,2,5,8) and gridlist[2] == 'O':
			return 'O'
		if checkPosition(gridlist,0,4,8) and gridlist[0] == 'O':
			return 'O'
		if checkPosition(gridlist,2,4,6) and gridlist[2] == 'O':
			return 'O'
		if checkPosition(gridlist,0,1,2) and gridlist[0] == 'X':
			return 'X'
		if checkPosition(gridlist,3,4,5) and gridlist[3] == 'X':
			return 'X'
		if checkPosition(gridlist,6,7,8) and gridlist[6] == 'X':
			return 'X'
		if checkPosition(gridlist,0,3,6) and gridlist[0] == 'X':
			return 'X'
		if checkPosition(gridlist,1,4,7) and gridlist[1] == 'X':
			return 'X'
		if checkPosition(gridlist,2,5,8) and gridlist[2] == 'X':
			return 'X'
		if checkPosition(gridlist,0,4,8) and gridlist[0] == 'X':
			return 'X'
		if checkPosition(gridlist,2,4,6) and gridlist[2] == 'X':
			return 'X'
		for i in gridlist:
			if i == ' ':
				return ' '
		return 'D'
	except:
		#print("here:")
		#print(gridlist)
		return None

def checkPosition(gridlist,p1,p2,p3):
	if gridlist[p1] == 'O' and gridlist[p2] == 'O' and gridlist[p3] == 'O':
		return True
	if gridlist[p1] == 'X' and gridlist[p2] == 'X' and gridlist[p3] == 'X':
		return True
	return False
