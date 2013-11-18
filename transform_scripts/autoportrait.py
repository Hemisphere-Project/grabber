#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, shutil, errno, subprocess


def copy(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def convert():
        # browse directories
	#for dirname, dirnames, filenames in os.walk('./compiled_media/autoportrait/orig'):
    		# print path to all filenames.
    		#for filename in filenames:
       			#print os.path.join(dirname, filename)
#mogrify -path ./resized/ -resize 400x300 *.jpg
	os.chdir('./compiled_media/autoportrait/orig')
	subprocess.call(["mogrify", "-path","../trans/","-resize","1000x1000","-blur","0x20","*.jpg"])
                	#print filename
                	#copy(dirname,'./users/'+str(user_id)+'/'+foldername)
	return

####################################################################################

if os.path.exists("./compiled_media/autoportrait/orig"):
	convert()
else:
	print "\n\n ./compiled_media/autoportrait not found\n\n"
	sys.exit(0)

####################################################################################



