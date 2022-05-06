import csv
import json
import urllib.request
def unique_values(k, lst):
  acc = []
  for x in lst:
    for key, val in x.items():
      if key == k:
        if val in acc:
          break
        else:
          acc.append(val)
  return acc
def filter_list(k, v, lst):
  acc = []
  for x in lst:
    if k in x and v == x[k]:
      acc.append(x)
  return acc
def dict_gen(keys, values):
  acc = {}
  index = 0
  for val in keys:
    acc[val] = values[index]
    index = index + 1
  return acc
def get_values(keys, dic):
  acc = []
  for val in keys:
    if val in dic.keys():
      acc.append(dic[val])
    else:
      break
  return acc
def header_reader(f_in):
  with open(f_in) as openf:
    csvread = csv.reader(openf)
    header = next(csvread)
    return header
def data_reader(f_in):
  acc = []
  with open(f_in) as openf:
    csvread = csv.reader(openf)
    next(csvread)
    for row in csvread:
      acc.append(row)
  return acc
def header_writer(lst, f_out):
  with open(f_out, "w") as openf:
    writer = csv.writer(openf)
    writer.writerow(lst)
def data_writer(lst, f_out):
  with open(f_out, "a") as openf:
    writer = csv.writer(openf)
    for item in lst:
      writer.writerow(item)
def clean_list(k, lst):
  acc = []
  for dic in lst:
    if k in dic:
      acc.append(dic)
  return acc
def cache_reader(f_in):
  with open(f_in) as openf:
    reader = list(csv.DictReader(openf, delimiter=',',quotechar='"'))
    return reader
def cache_writer(lst, f_out):
  for dic in lst:
    header_writer(dic, f_out)
  header = header_reader(f_out)
  with open(f_out, "a") as openf:
    writer = csv.writer(openf)
    for dic in lst:
      acc = []
      for head in header:
        val = dic[head]
        acc.append(val)
      writer.writerow(acc)
def retrieve_json(url):
  req = urllib.request.urlopen(url)
  response = req.read().decode()
  actual_data = json.loads(response)
  return actual_data
