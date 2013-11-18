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
	os.chdir('./compiled_media/paysage/orig')
	subprocess.call(["mogrify", "-path","../trans/","-resize","1600x1600","*.jpg"])
	return

####################################################################################

if os.path.exists("./compiled_media/paysage/orig"):
	convert()
else:
	print "\n\n ./compiled_media/paysage not found\n\n"
	sys.exit(0)

####################################################################################



