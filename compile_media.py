#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, shutil, errno
import xml.etree.cElementTree as ET


def createXMLFile(dir):
	root = ET.Element("files")
	tree = ET.ElementTree(root)
	tree.write(dir+"/fileslist.xml")

def appendFileToXML(dir,filename):
	tree = ET.parse(dir+"/fileslist.xml")
        root = tree.getroot()
	filenode = ET.SubElement(root,"file")
	filenode.text = filename
	tree.write(dir+"/fileslist.xml")

def copy(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def compile_media():
        # browse directories
	for dirname, dirnames, filenames in os.walk('./users'):
    		# print path to all subdirectories first.
    		#for subdirname in dirnames:
			#print "-----------------------------------------"
        		#print os.path.join(dirname, subdirname)

    		# print path to all filenames.
    		for filename in filenames:
       			#print os.path.join(dirname, filename)
			if dirname.find("2. Paysage")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/paysage/orig")
				appendFileToXML("./compiled_media/paysage",filename)
			if dirname.find("3. Instantan")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/instantane/orig")
				appendFileToXML("./compiled_media/instantane",filename)
			if dirname.find("5. Nature morte")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/nature_morte/orig")
				appendFileToXML("./compiled_media/nature_morte",filename)
			if dirname.find("7. Conversation")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/conversation/orig")
				appendFileToXML("./compiled_media/conversation",filename)
			if dirname.find("8. Portrait")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/portrait/orig")
				appendFileToXML("./compiled_media/portrait",filename)
			if dirname.find("9. Autoportrait")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/autoportrait/orig")
				appendFileToXML("./compiled_media/autoportrait",filename)
			if dirname.find("11. Silence")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/silence/orig")
				appendFileToXML("./compiled_media/silence",filename)
			if dirname.find("14. Voix")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/voix/orig")
				appendFileToXML("./compiled_media/voix",filename)
			if dirname.find("15. Nu")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/nu/orig")
				appendFileToXML("./compiled_media/nu",filename)
			if dirname.find("Prendre une photo")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/photo_test/orig")
				appendFileToXML("./compiled_media/photo_test",filename)
			if dirname.find("Enregistrer un son")!=-1:
				copy(os.path.join(dirname,filename),"./compiled_media/son_test/orig")
				appendFileToXML("./compiled_media/son_test",filename)
			
                	#print filename
                	#copy(dirname,'./users/'+str(user_id)+'/'+foldername)
	return

####################################################################################

# clean 

if os.path.exists("./compiled_media"):
	print "\n\ncleaning compiled_media directory\n\n"
	shutil.rmtree("./compiled_media")
# create dirs and xml files
os.makedirs("./compiled_media");

os.makedirs("./compiled_media/paysage");
os.makedirs("./compiled_media/paysage/orig");
os.makedirs("./compiled_media/paysage/trans");
createXMLFile("./compiled_media/paysage")

os.makedirs("./compiled_media/instantane");
os.makedirs("./compiled_media/instantane/orig");
os.makedirs("./compiled_media/instantane/trans");
createXMLFile("./compiled_media/instantane")

os.makedirs("./compiled_media/nature_morte");
os.makedirs("./compiled_media/nature_morte/orig");
os.makedirs("./compiled_media/nature_morte/trans");
createXMLFile("./compiled_media/nature_morte")

os.makedirs("./compiled_media/conversation");
os.makedirs("./compiled_media/conversation/orig");
os.makedirs("./compiled_media/conversation/mp3");
createXMLFile("./compiled_media/conversation")

os.makedirs("./compiled_media/portrait");
os.makedirs("./compiled_media/portrait/orig");
os.makedirs("./compiled_media/portrait/trans");
createXMLFile("./compiled_media/portrait")

os.makedirs("./compiled_media/autoportrait");
os.makedirs("./compiled_media/autoportrait/orig");
os.makedirs("./compiled_media/autoportrait/trans");
createXMLFile("./compiled_media/autoportrait")

os.makedirs("./compiled_media/silence");
os.makedirs("./compiled_media/silence/orig");
os.makedirs("./compiled_media/silence/mp3");
createXMLFile("./compiled_media/silence")

os.makedirs("./compiled_media/voix");
os.makedirs("./compiled_media/voix/orig");
os.makedirs("./compiled_media/voix/trans");
createXMLFile("./compiled_media/voix")

os.makedirs("./compiled_media/nu");
os.makedirs("./compiled_media/nu/orig");
os.makedirs("./compiled_media/nu/trans");
createXMLFile("./compiled_media/nu")

os.makedirs("./compiled_media/photo_test");
os.makedirs("./compiled_media/photo_test/orig");
os.makedirs("./compiled_media/photo_test/trans");
createXMLFile("./compiled_media/photo_test")

os.makedirs("./compiled_media/son_test");
os.makedirs("./compiled_media/son_test/orig");
os.makedirs("./compiled_media/son_test/mp3");
createXMLFile("./compiled_media/son_test")

compile_media()
sys.exit(0)

####################################################################################


