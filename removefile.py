import subprocess 
import glob
import os
import sys 
if sys.platform == 'linux':
	pass
else:
	os.exit()
get_cache = glob.glob('.cache*')
if len(get_cache) == 0:
	print('Not found cache. CONTINUE')
else:
	for i in get_cache:
		bash_command = "sudo rm -r "+str(i);
		process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
try:
	os.chdir('photos')
except:
	print('Folder photos not exist. EXIT')
	os.exit()
get_jpg = glob.glob('*.jpg')
if len(get_jpg) == 0:
	print('Photos  folder is empy. EXIT')
	os.exit()
else:
	for j in get_jpg:
		bash_command = "sudo rm -r "+str(j);
		process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()

