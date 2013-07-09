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


#	this is a prog which appends a list to another
def main():
	li=[]
	k=input("enter no. of elements in list 1:")
	i=int(k)
	l=1
	print("enter the elements in list 1")
	while(l<=i):		
	    j=input() 
	    li.append(j)
	    l+=1
	print("list 1:")
	print(li)
	k=input("enter no. of elements in list 2:")
	i=int(k)
	l=1
	lin=[]
	while(l<=i):
		j=input()
		lin.append(j)
		l+=1
	print("list 2:")
	print(lin)
	li.extend(lin)
	print("the appended list 1:")
	print(li)
	return 0

if __name__ == '__main__':
	main()
