from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from django.http import HttpResponseBadRequest


@csrf_exempt
def index(request):
	if request.META.get('CONTENT_TYPE') == 'application/json':
		if request.method == 'POST':
			griddict = json.loads(request.body.decode('utf8'))
			
			new_griddict = processGrid(griddict)
			#print(new_griddict)
			return HttpResponse(json.dumps(new_griddict).encode('utf8'),content_type="application/json")
	return HttpResponse("")
def processGrid(griddict):
	#print(checkWinner(griddict['grid']))
	#if winner in griddict:
		#return griddict
	check = False
	for i in range(0,9):
		if griddict['grid'][i] == ' ':
			check = True
	if not check:
		griddict['winner']=' '
		return griddict
	
	w  = checkWinner(griddict['grid'])
	
	if w != '':
		griddict['winner'] = w
	
	if w  == '':
		if griddict['grid'][4] == ' ':
			griddict['grid'][4] = 'O'
			w = checkWinner(griddict['grid'])	
		else:
			if checkWinningSpot(griddict['grid'])!=-1:
				s = checkWinningSpot(griddict['grid'])
				griddict['grid'][s] = 'O'
				w = checkWinner(griddict['grid'])
				if w != '':
					griddict['winner'] = w
			else:	
				griddict['grid'][griddict['grid'].index(' ')] = 'O'
				w = checkWinner(griddict['grid'])
				if w != '':
					griddict['winner'] = w
	return griddict

def checkWinningSpot(gridlist):
	if checkPosition2(gridlist,0,1,2) != -1:
		return checkPosition2(gridlist,0,1,2)
	if checkPosition2(gridlist,3,4,5) != -1:
		return checkPosition2(gridlist,3,4,5)
	if checkPosition2(gridlist,6,7,8) != -1:
		return checkPosition2(gridlist,6,7,8)
	if checkPosition2(gridlist,0,3,6) != -1:
		return checkPosition2(gridlist,0,3,6)
	if checkPosition2(gridlist,1,4,7) != -1:
		return checkPosition2(gridlist,1,4,7)
	if checkPosition2(gridlist,2,5,8) != -1:
		return checkPosition2(gridlist,2,5,8)
	if checkPosition2(gridlist,0,4,8) != -1:
		return checkPosition2(gridlist,0,4,8)
	if checkPosition2(gridlist,2,4,6) != -1:
		return checkPosition2(gridlist,2,4,6)
	if checkPosition3(gridlist,0,1,2) != -1:
		return checkPosition3(gridlist,0,1,2)
	if checkPosition3(gridlist,3,4,5) != -1:
		return checkPosition3(gridlist,3,4,5)
	if checkPosition3(gridlist,6,7,8) != -1:
		return checkPosition3(gridlist,6,7,8)
	if checkPosition3(gridlist,0,3,6) != -1:
		return checkPosition3(gridlist,0,3,6)
	if checkPosition3(gridlist,1,4,7) != -1:
		return checkPosition3(gridlist,1,4,7)
	if checkPosition3(gridlist,2,5,8) != -1:
		return checkPosition3(gridlist,2,5,8)
	if checkPosition3(gridlist,0,4,8) != -1:
		return checkPosition3(gridlist,0,4,8)
	if checkPosition3(gridlist,2,4,6) != -1:
		return checkPosition3(gridlist,2,4,6)
	return -1

def checkPosition2(gridlist,p1,p2,p3):
	if gridlist[p1] == 'O' and gridlist[p2] == 'O' and gridlist[p3] == ' ':
		return p3
	if gridlist[p1] == ' ' and gridlist[p2] == 'O' and gridlist[p3] == 'O':
		return p1
	if gridlist[p1] == 'O' and gridlist[p2] == ' ' and gridlist[p3] == 'O':
		return p2
	return -1

def checkPosition3(gridlist,p1,p2,p3):
	if gridlist[p1] == ' ' and gridlist[p2] == 'X' and gridlist[p3] == 'X':
		return p1
	if gridlist[p1] == 'X' and gridlist[p2] == ' ' and gridlist[p3] == 'X':
		return p2
	if gridlist[p1] == 'X' and gridlist[p2] == 'X' and gridlist[p3] == ' ':
		return p3	
	return -1

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
				return ''
		return ' '
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
