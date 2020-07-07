import sys
import datetime
time=datetime.datetime.now()
url=sys.argv[1]
output= "%s time is %s" % (url,time)
print(output.rstrip())
#print (''.join(output)