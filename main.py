import bottle
import json
import data
import os.path
import urllib.request
import csv
@bottle.route('/')
def index():
  html_file = bottle.static_file("index.html")
  return html_file
@bottle.route('/ajax')
def jscode():
  jscode = bottle.static_file("ajax.js")
  return jscode
def load_data():
   csv_file = 'cache.csv'
   if not os.path.isfile(csv_file):
      url = 'https://data.cityofnewyork.us/resource/uip8-fykc.json?$limit=50000&$select=arrest_date,pd_desc,ofns_desc,arrest_boro,arrest_precinct,law_cat_cd,age_group,perp_sex,perp_race'
      info = data.retrieve_json(url)
  	  needed_keys = ['arrest_date','age_group','arrest_boro','pd_desc','law_cat_cd']
	    for k in needed_keys :
    	  info = data.clean_list(k, info)
  	  data.cache_writer(info, csv_file)
load_data()
def dates(f_in):
  dates = []
  lsts = data_reader(f_in)
  for lst in lsts:
    date = lst[0]
    if date not in dates:
      dates.append(date)
  dates.sort()
  dateamount={}
  for date in dates:
    dateamount[date] = 0
  for lst in lsts:
    datadate = lst[0]
    if datadate in dateamount:
      dateamount[datadate] = int(dateamount[datadate]) + 1
  return dateamount
def boros(f_in):
  borocount={'B':0,'K':0,'Q':0,'M':0,'S':0,}
  lsts = data_reader(f_in)
  for lst in lsts:
    boro = lst[3]
    if boro in borocount:
      borocount[boro] = int(borocount[boro]) + 1
  return borocount
def agecount(targetboro, f_in):
  groups = []
  lsts = data_reader(f_in)
  for lst in lsts:
    group = lst[6]
    if group not in groups:
      groups.append(group)
  val = {}
  for group in groups:
    val[group] = 0
  for lst in lsts:
    boro = lst[3]
    if boro == targetboro:
      group = lst[6]
      val[group] = int(val[group]) + 1
  return val
def data_reader(f_in):
  acc = []
  with open(f_in) as openf:
    csvread = csv.reader(openf)
    next(csvread)
    for row in csvread:
      acc.append(row)
  return acc
@bottle.get('/linegraph')
def linegraph():
  linedata = dates("cache.csv")
  return json.dumps(linedata)
@bottle.get('/piechart')
def piechart():
  piedata = boros("cache.csv")
  return json.dumps(piedata)
@bottle.post('/barchart')
def handle_post():
  content = bottle.request.body.read()
  json_content = content.decode()
  content = json.loads(json_content)
  bardata = agecount(json_content, "cache.csv")
  json_blob = json.dumps(bardata)
  return json_blob
bottle.run(host="0.0.0.0", port=8080)
