#!/usr/bin/python

import os, sys, shutil, errno


def copy(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def get_folder_name(filename):
	# Open the html file
	fo = open("./users/"+str(user_id)+"/"+str(user_id), "r")

	#read the content of the file
	file_str = fo.read();
	#print "Read String is : ", str

	file_index = file_str.find(filename)
	if(file_index !=-1):
		#initially we'd like to use a rfind but it would have to return the first occurence
		#in order to work
        	#title_index_start = file_str.rfind("<h2>",file_index)
		# the following has to be tested !!
		#print "file_index  ",file_index
		step=count=10
		while file_str.find("<h2>",file_index-count,file_index) ==-1:
			count+=10
			#print "sub     ",file_index-count,"    ",file_index,"   ",file_str[file_index-count:file_index-count+step]
        	# the following line doesn't work cause it can cut the <h2>
		#title_index_start = file_str.find("<h2>",file_index-count,file_index-count+step)
		title_index_start = file_str.find("<h2>",file_index-count,file_index)
		
		if(title_index_start !=-1):
			#print "title_index_start   ",title_index_start
                	title_index_stop = file_str.find("</h2>",title_index_start)
                	if(title_index_stop !=-1):
                        	title = file_str[title_index_start+4:title_index_stop]
                        	#print "THE TITLE : ",title
                	else:
                        	print "title stop not found"
				return -1
        	else:
                	print "title start not found"
			return -1
	else:
        	print "string not found"
		return -1

	# Close opend file
	fo.close()

	return title

def rename_media():
        # browse directories
	for dirname, dirnames, filenames in os.walk('./users/'+str(user_id)+'/data/files'):
    		# print path to all subdirectories first.
    		#for subdirname in dirnames:
        		#print os.path.join(dirname, subdirname)

    		# print path to all filenames.
    		for filename in filenames:
			print "-----------------------------------------"
        		print os.path.join(dirname, filename)
                	print filename
                	foldername = get_folder_name(filename)
                	if foldername == -1: sys.exit(0)
               		foldername = foldername.replace('/','-')
                	print foldername
                	#os.chdir(dirname)
                	#print os.getcwd()
                	#os.rename(dirname,'./users/'+str(user_id)+'/'+foldername)
                	copy(dirname,'./users/'+str(user_id)+'/'+foldername)
	return

####################################################################################

if len(sys.argv) < 2:
    print("enter a user id as first argument")
    sys.exit(0)

user_id  = sys.argv[1]
#user_id=14

if(os.path.exists('./users/'+str(user_id))):
	rename_media()
else:
	print "U S E R   D O E S N T   E X I S T"
	sys.exit(0)

####################################################################################

