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
	for dirname, dirnames, filenames in os.walk('./compiled_media/conversation/orig'):
    		# print path to all filenames.
    		for filename in filenames:
       			print os.path.join(dirname, filename)
			subprocess.call(["ffmpeg", "-i",os.path.join(dirname,filename),dirname+"/../mp3/"+filename.split('.')[0]+".mp3"])
                	#print filename
                	#copy(dirname,'./users/'+str(user_id)+'/'+foldername)
	return

####################################################################################

if os.path.exists("./compiled_media/conversation/orig"):
	convert()
else:
	print "\n\n ./compiled_media/conversation not found\n\n"
	sys.exit(0)

####################################################################################



