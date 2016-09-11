#!/usr/bin/env python

USER_ID_IDX=1

import csv
import numpy as np

class User(list):
	def __init__(this, id):
		this.id = id
		pass

def getFile(filepath):
	userDict = {}
        labelNames = []
	with open(filepath, 'r') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for idx,row in enumerate(filereader):
                        if(idx==0):
                                labelNames = row
                                continue
			userid = row[USER_ID_IDX]
			if(not userid in userDict):
				userDict[userid] = User(userid)
			userDict[userid].append(row)
	return userDict,labelNames

def getFileTrain(filepath, outputfilepath):
	userDict = {}
        labelNames = []
	with open(filepath, 'r') as csvfile, open(outputfilepath, 'r') as outputfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for idx,row in enumerate(filereader):
                        outputline = outputfile.readline().rstrip()
                        if(idx==0):
                                labelNames = row
                                continue
                        outputparse = outputline.split(',')
                        if(outputparse[0] != row[0]):
                                print('error: l'+str(idx))
                        row.append(outputparse[1])
			userid = row[USER_ID_IDX]
			if(not userid in userDict):
				userDict[userid] = User(userid)
			userDict[userid].append(row)
	return userDict,labelNames
