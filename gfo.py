#!/usr/bin/env python
# -*- coding: utf-8 -*-
#gfo gallery generator ver. 0.2 by grizz - Witek Firlej http://grizz.pl
# Copyright (C) 2009-2010 Witold Firlej
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

__project__	= "gfo gallery generator"
__author__	= "Witold Firlej (http://grizz.pl)"
__version__	= "0.26"
__license__	= "GPL3"
__copyright__	= "Witold Firlej"

import sys,ConfigParser,glob,Image

INDEXTITLE = "" ###XXX remove globals 
FOOTER = ""


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
							+ "-o\t OneShotMode - generate index.html in current folder"

	except IndexError:
		pass

def verbose (msg):
	try:
		if sys.argv[1] == "-v":
			print msg;
	except IndexError:
		pass
		
def generateAlbumPropFile ():				###TODO maybe in the future to entitle and descroibe each photo
	"""
	Generate file with each album properties inside album folder
	"""

def getAlbumsConfig ():
	""" 
	Get albums config from main conf file 

	@return a list with properties
	"""
	config = ConfigParser.ConfigParser()
	config.read("gfo.conf")

	global INDEXTITLE 							###XXX remove globals 
	global FOOTER
	INDEXTITLE = config.get("main", "indextitle")
	FOOTER = config.get("main", "footer")
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

# przeskanuj listę  dla każdego albumu wpisz nazwe z desc jako nazwe liku do strony name.html i zapisz to do stringa, który potem bedzie wstawiony w [[[ALBUMSLIST]]]
	ALBUMSLIST = "|| "
	for name, desc, folder in albumslist: 			### Generate albumlist
		ALBUMSLIST += "<a href=\"" + name + ".html\">" + desc + "</a> || "

	for name, desc, folder in albumslist: 			### generate each subpage
		verbose("===============\n")
		verbose("Album's name:\t" + name)
		verbose("Album's description:\t" + desc)
		verbose("Album's folder:\t" + folder)
		verbose("===============\n")

		#weź sprawdź folder i dla każdego zdjęcia (jpg|JPG) w folderze
		### Dodaj do stringa wstawianego w miejsce [[[FOTO]]] string zawierajacy cały kod htmla jednego zdjecia
		i = 1														# itterator for inserting new line<p>
		FOTO = "<p>"
		files = glob.glob(folder + "/*.[jJ][pP][gG]")       # list both .jpg and JPG
		files.sort() 									# sort files alphabetically
		for infile in files:
			thumb = makethumb(infile)
			FOTO += "<a href=\""+ infile + "\" alt=\"kliknij lewym przyciskiem / left click, please\" onclick=\"return hs.expand(this)\"><img src=\"" + thumb + "\" alt=\"photo\" /></a>\n"
			if i%6==0: 											# only 6 images in each row
				FOTO +="<p>"
			i += 1

			verbose(FOTO) ###XXX DEBUG

		albumtemplate = open("albumindex.html.tpl").readlines()
		albumdest = open(name + ".html", 'w')
		for s in albumtemplate:
			if s.find("[[[ALBUMTITLE]]]") != -1:
				albumdest.write(s.replace("[[[ALBUMTITLE]]]", desc + " :: " + INDEXTITLE))
			elif s.find("[[[ALBUMSLIST]]]") != -1:
				albumdest.write(s.replace("[[[ALBUMSLIST]]]", ALBUMSLIST))
			elif s.find("[[[FOOTER]]]") != -1:
				albumdest.write(s.replace("[[[FOOTER]]]", FOOTER))
			else:
				albumdest.write(s.replace("[[[FOTO]]]", FOTO))
		albumdest.close()
	

 		# weź wygeneruj index.html kapiujac FIRSTALBUM jako index, czyli w sumie index.html.tpl jest niepotrzebny jak narazie
		albumtemplate = open("index.html.tpl").readlines()
		albumdest = open("index.html", 'w')
		for s in albumtemplate:
			if s.find("[[[INDEXTITLE]]]") != -1:
				albumdest.write(s.replace("[[[INDEXTITLE]]]", INDEXTITLE)) 
			elif s.find("[[[ALBUMSLIST]]]") != -1:
				albumdest.write(s.replace("[[[ALBUMSLIST]]]", ALBUMSLIST))
			elif s.find("[[[FOOTER]]]") != -1:
				albumdest.write(s.replace("[[[FOOTER]]]", FOOTER))
			else:
				albumdest.write(s.replace("[[[FIRSTALBUM]]]", albumslist[0][0] + ".html")) 	#use album with index == 1 as firstalbum
		albumdest.close()


def oneShot():
	"""
	OneShotMode
	"""
	print "Bang"


def makethumb(infile):
	"""
	Make square thumbnail and 
	@returtn thumb name
	"""
	THUMB_SIZE = 125, 125

	img = Image.open(infile)
	width, height = img.size

	if width > height:
		delta = width - height
		left = int(delta/2)
		upper = 0
		right = height + left
		lower = height
	else:
		delta = height - width
		left = 0
		upper = int(delta/2)
		right = width
		lower = width + upper
	img = img.crop((left, upper, right, lower))
	img.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
	outfile = infile[:-4] + "_thumb.jpeg" 					### allow to skip generate thumnails of thumbnails
	#print infile + " ==> " + outfile
	img.save(outfile, "JPEG")
	return outfile

def main ():
	""" main loop """
	#help()
	try:
		if sys.argv[1] == "--help":
			help()
		elif sys.argv[1] == "-o":
			oneShot()
	except:
		generateGallery(getAlbumsConfig())
main() # run main loop
