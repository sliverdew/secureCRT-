#/bin/sh
# -*- coding: utf-8 -*-
import re
import shutil,os
if not os.path.exists('CRT PORT'):
	os.mkdir('CRT PORT')
path_origin = os.getcwd()
path_new = os.getcwd()+'\\'+'CRT PORT'
with open(path_origin+'\\'+'port.txt',"r") as f:
	fline = f.readlines()
OBJ = fline[0].replace('\n','')
BAUD_RATE = int(fline[1])
for i in range(len(fline)-2):
	shutil.copyfile(path_origin+'\\'+'default.ini',path_new+'\\'+OBJ+'_'+fline[i+2].replace('\n','')+'.ini')
Num1 = os.listdir(path_new)
for j in range(len(Num1)):
	file = path_new+'\\'+Num1[j]
	with open(file,'r+') as f1,open("%s.bak" % file, "w") as f2:
		if BAUD_RATE == 115200:
			for line in f1:
				f2.write(re.sub(r'\"Baud Rate\"=(.+)','\"Baud Rate\"=0001c200',line))
		elif BAUD_RATE == 1500000:
			for line in f1:
				f2.write(re.sub(r'\"Baud Rate\"=(.+)','\"Baud Rate\"=0016e360',line))
		else :
			print("Your baud rate is not defined,please modify the default configuration file")
	os.remove(file)
	os.rename("%s.bak" % file, file)
j = 0
Num2 = os.listdir(path_new)
for j in range(len(Num2)):
	port = Num2[j].split('.')[0].split('M')[1]
	file = path_new+'\\'+Num2[j]
	with open(file,'r+') as f1,open("%s.bak" % file, "w") as f2:
		for line in f1:
			f2.write(re.sub(r'\"Com Port\"=(.+)',r'"Com Port"=COM'+port,line))
	os.remove(file)
	os.rename("%s.bak" % file, file)