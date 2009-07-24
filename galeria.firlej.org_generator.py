#!/usr/bin/env python
# -*- coding: utf-8 -*-
#galeria.firlej.org generator ver. 0.1 by grizz - Witek Firlej http://grizz.pl
# Copyright (C) 2009 Witold Firlej
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

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
	# przeskanuj listę  dla każdego albumu wpisz nazwe z desc jako nazwe liku do strony name.html i zapisz to do stringa, który potem bedzie wstawiony w [[[ALBUMSLIST]]]

	for name, desc, folder in albumslist:
		verbose("Album's name:\t" + name)
		verbose("Album's description:\t" + desc)
		verbose("Album's folder:\t" + folder)
		verbose("===")
		#weź sprawdź folder i dla każdego zdjęcia (jpg|JPG) w folderze
		### Dodaj do stringa wstawianego w miejsce [[[FOTO]]] string zawierajacy cały kod htmla jednego zdjecia
		# weź albumslist.html.tpl i w miesce [[[foto]]] wstaw powyżej wygenerowany string a w miejsce [[[ALBUMTITLE]]] wstaw string wygenerowany w poprzedniej pętli.
		
 		# weź wygeneruj index.html kapiujac FIRSTALBUM jako index, czyli w sumie index.html.tpl jest niepotrzebny jak narazie
def main ():
	""" main loop """
	#help()
	generateGallery(getAlbumsConfig())

main() # run main loop
