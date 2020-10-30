import flask
import datetime
from flask import jsonify,request
import pandas as pd 
import numpy as np
app = flask.Flask(__name__)
app.config["DEBUG"] = True
input1 = {
	'responses':{
		'Response-id-1':{
			'Score':8,
			'Date':'2020-10-15'
		},
		'Response-id-2':{
			'Score':9,
			'Date':'2020-10-15'
		},
		'Response-id-3':{
			'Score':10,
			'Date':'2020-10-16'
		},
		'Response-id-4':{
			'Score':9,
			'Date':'2020-10-16'
		},
		'Response-id-5':{
			'Score':0,
			'Date':'2020-10-17'
		},
		'Response-id-6':{
			'Score':1,
			'Date':'2020-10-18'
		},
		'Response-id-7':{
			'Score':3,
			'Date':'2020-10-17'
		},
		'Response-id-8':{
			'Score':7,
			'Date':'2020-10-17'
		},
		'Response-id-9':{
			'Score':8,
			'Date':'2020-10-17'
		},
		'Response-id-10':{
			'Score':10,
			'Date':'2020-10-18'
		},
		'Response-id-11':{
			'Score':7,
			'Date':'2020-10-18'
		},
		'Response-id-12':{
			'Score':5,
			'Date':'2020-10-17'
		},
		'Response-id-13':{
			'Score':0,
			'Date':'2020-10-16'
		},
		'Response-id-14':{
			'Score':0,
			'Date':'2020-10-15'
		},
		'Response-id-15':{
			'Score':10,
			'Date':'2020-10-15'
		},
	}
}
""" result1 ={
	"date":{
		"Promotors":
		"Passives":
		"Detractors":
	}
}"""
"""
result = {
	"Date" =[list of scores]
}"""
result = {}
a = input1['responses'].keys()
for response in a:
	#result[response]=input1[response]
	result[input1['responses'][response]['Date']] =[] 
for response in a:
	result[input1['responses'][response]['Date']].append(input1['responses'][response]['Score'])
result1 = {}
a = result.keys()
for date in a:
	result1[date] = {
	'Promoters'  : 0,
    'Passives' : 0, 
    'Detractors': 0
	}
for date in a:
	lis = result[date]
	for ele in lis :
		if ele <=6:
			result1[date]['Detractors'] = result1[date]['Detractors']+1
		elif ele<9 :
			result1[date]['Passives'] = result1[date]['Passives']+1
		else :
			result1[date]['Promoters'] = result1[date]['Promoters']+1
@app.route('/',methods=['GET'])
def home():
	return jsonify(input1)

@app.route('/apps_details',methods=['GET']) # 
def all():
	apps_details = result
	return jsonify(apps_details)
@app.route('/getnps',methods=['GET'])
def required_output():
	if 'startDate' in request.args:
		startDate = datetime.datetime.strptime(request.args['startDate'],'%Y-%m-%d')
	if 'endDate' in request.args:
		endDate = datetime.datetime.strptime(request.args['endDate'],'%Y-%m-%d')
	delta = datetime.timedelta(days=1)
	res={'Result':{}}
	curr = 0
	while(startDate<=endDate):
		t = startDate
		response ={}
		t = t.strftime('%Y-%m-%d')
		curr = curr+1
		response = result1[t]
		res['Result'][t] = response
		startDate+=delta	

	return jsonify(res)

@app.route('/get_nps_score',methods=['GET'])
def calc(): #function to calculate json Score           details----> nps score
	if 'startDate' in request.args:
		startDate = datetime.datetime.strptime(request.args['startDate'],'%Y-%m-%d')
	if 'endDate' in request.args:
		endDate = datetime.datetime.strptime(request.args['endDate'],'%Y-%m-%d')
	delta = datetime.timedelta(days=1)
	res={'Result':{}}
	curr = 0
	while(startDate<=endDate):
		response={}
		t = startDate
		t = t.strftime('%Y-%m-%d')
		curr = curr+1
		promoters = result1[t]['Promoters']
		passives = result1[t]['Passives']
		detractors = result1[t]['Detractors']
		nps_score = ((promoters - detractors)/(promoters + detractors + passives) )*100
		nps_score = int(nps_score)
		response['NPS_Score'] = nps_score
		res['Result'][t] = response
		startDate+=delta
	return jsonify(res)



app.run()

