#!/usr/python
#
# I dedicate this application for my best friend, Robert Niemiec :)
#
# Copyright (c) 2015 Dawid Wiktor
# This app is writed for all whistleblowers, journalists and 
# cryptoanarchists. Use it when you need. Be carefull! NSA watchin'
# 
# This is the Open Source Software. You can freely use it, edit code, and 
# ditribute. But you should respect Attribution.

def encryption():
	key = input("Please, input a number here to be used as the key.\n")
	key = int(key)
	dummy = 0
	rawData = input("Enter string here.\n")
	rawlist = list(rawData)
	data = rawlist[0 + dummy]
	number = len(rawlist)

	while dummy != number:
		data = ord(data)
		data = data + key
		print(data)
		dummy = dummy + 1
		data = rawlist[0 + dummy]

run = "y"
while run == "y":
	encryption()
	run = input("Do you want to encrypt this? (y/n)\n")

if run !="y":
	exit()
