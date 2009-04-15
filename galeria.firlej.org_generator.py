#!/usr/bin/env python
# -*- coding: utf-8 -*-
#galeria.firlej.org generator ver. 0.1 by grizz - Witek Firlej http://grizz.pl

__project__	= "galeria.firlej.org generator"
__author__	= "Witold Firlej (http://grizz.pl)"
__version__	= "0.1"
__license__	= "GPL"
__copyright__	= "Witold Firlej"

import os,sys,ConfigParser

def about ():
	"""About project"""
	about = "______________\n" + __project__ + " ver. " + __version__ + " by " + __author__ + "\n\n"
	return about

def help ():
	""" Printing help """
	print about()
	try:
		if sys.argv[1] == "--help":
			print "OPTIONS:\n" \
							+ "--help\t Print this information\n" \
							+ "-v\t Be verbose\n" \
							+ "-p filename\t Generate albumPropFile with album properties\n" \
							+ "-l\t show albums list\n" \
							+ "-g albumPropFile\t Generate whole gallery"
	except IndexError:
		pass

def verbose (msg):
	try:
		if sys.argv[1] == "-v":
			print msg;
	except IndexError:
		pass
		
def generateAlbumPropFile ():				###TODO maybe in the futere to entitle and descroibe each photo
	"""
	Generate file with each album properties inside album folder
	"""

def getAlbumsConfig ():
	""" 
	Get albums config from main conf file 

	@return a list with properties
	"""
	config = ConfigParser.ConfigParser()
	config.read("galeria.firlej.org.conf")
	albumslist = []
	for section in config.sections():
		if not section == "main": 			# skip main section
			album = (config.get(section, "name"), config.get(section, "desc"), config.get(section, "folder"))
			albumslist.append(album)
	return albumslist

def generateGallery(albumslist):
	"""
	Generate whole gallery 
	"""
	print albumslist
	for name, desc, folder in albumslist:
		verbose("Album's name:\t" + name)
		verbose("Album's description:\t" + desc)
		verbose("Album's folder:\t" + folder)
		verbose("===")

def main ():
	""" main loop """
	#help()
	generateGallery(getAlbumsConfig())

main() # run main loop
