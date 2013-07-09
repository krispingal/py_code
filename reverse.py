#!/usr/bin/env python3.1
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2010 Krishna Pingal B <krishna@kris-laptop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.




def main():
	#to input a string & 2 print it's reverse
	a = "asdasd"	
	a = input('enter a string :')
	print ("%s" %a)	
	rev=a[::-1]
	print("the reverse of the string is {0}".format(rev))
	
	return 0

if __name__ == '__main__':
	main()
