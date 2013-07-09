#!/usr/bin/env python
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



	#prog 2 find n'th prime no.
list_of_primes = [2,]
count 	= 1
current = 3
n=input("enter the val of n ")
while (count < n) : 
	# check if current is a prime
	# if prime:
	#	list_of_primes.append ( current )
	#	count = count + 1
	# current = current + 1
	flag=1
	for i in list_of_primes:
		p
		if (current%i==0):
			flag=0
			break
	
	if flag == 1 :
		list_of_primes.append(current)
		count+=1
	current+=1

print current-1 
print list_of_primes
print "The nth prime is %d" %list_of_primes[count-1]
