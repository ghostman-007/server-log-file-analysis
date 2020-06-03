import os
from datetime import datetime

with open('access.log') as f:
	d = {}
	for n, line in enumerate(f):
		fields = line.strip().split()
		#print(fields[0] + " " + fields[3] + " " + fields[4])
		time = fields[3].split(':',1)[1]
		print(fields[0] + " " + time)
		t2 = '04:38:50'
		t1 = '04:38:50'
		FMT = '%H:%M:%S'
		time_diff = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
		millisec = time_diff.total_seconds()
		print(millisec)
		# check count
		#if count > 150:
		#	#DENY
		#else:
		#	count += 1
		#d[fields[0]] = [fields[3]]
	#print(d)

	# Deny attacker ip address
	#os.system(sudo ufw deny from <ip> to any
