# paraglider.py
# by foulenzer

# import stuff
import warnings
import sys
import re
from functions import requestContent, parseContent

# ignore openSSL warnings
warnings.filterwarnings("ignore")

# prepare stuff
count = 0
body  = ''

# Looks beatiful, no?
print('### paraglider.py - parameter discovery ###')
print('# Checking subject_list #')

# get subject
try:
	subject_list = open(sys.argv[1], 'rb').readlines()
except:
	print('Sir, something is wrong with the subject argument. x(')
else:
	for subject in subject_list:
		print(subject.strip())
		try:
			content = requestContent('GET', 'https://' + subject.strip(), '')
		except:
			try:
				content = requestContent('GET', 'http://' + subject.strip(), '')
			except:
				print('Sir, something is wrong with the domain parameter.')
			else:
				parseContent(content)
		else:
			parseContent(content)