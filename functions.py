# functions.py

# import stuff
import warnings
import requests
import re

# ignore openSSL warnings
warnings.filterwarnings("ignore")

# function request_body()
# getting the body data of an http request
# parameter:
#	- type    -> request type (GET or POST)
#	- subject -> subject to run scan on
#	- data    -> json data for POST requests
def requestContent(reqtype, subject, data):
	if reqtype == 'GET':
		try:
			req = requests.get(subject, timeout=5)
		except:
			print('Sir, could not send request. Is host up?')
			return 'FALSE'
		else:
			return req.content
	elif reqtype == 'POST':
		try:
			req = requests.post(subject, data = {data}, timeout=5)
		except:
			print('Sir, could not send request. Status code: ' + req.status_code)
			return 'FALSE'
		else:
			return req.content
	else:
		print('Sir, something went wrong with the type parameter.')
		return 'FALSE'

# function parseContent()
# find pattern in source code of http request
# parameter:
#	- reqcontent -> source code as string
def parseContent (reqcontent):
	regex_list = [
		'<input',
		'action=',
	]
	generic_regex = re.compile( '|'.join( regex_list) )
	try:
		line_list = (reqcontent.decode(encoding='UTF-8')).splitlines()
	except:
		line_list = str(reqcontent).splitlines()
	for line in line_list:
		if len(line) > 1024:
			continue
		match = re.search(generic_regex, line)
		if match:
			print('[Found possible parameter]' + match.string.strip())
