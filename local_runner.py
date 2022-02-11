import sys
from app.f5_mig import *

if len(sys.argv)>1:
	file_names=sys.argv[1:]
else:
	file_names=input("C:\Users\Singhsabh\Desktop\BOI\Radware f5\n").replace('"','')

c=0
for i in file_names:
	fun_f5_mig(i, 'local_'+str(c), 0)
	c+=1
