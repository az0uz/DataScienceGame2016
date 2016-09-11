#!/usr/bin/env python

import urllib2
from time import sleep
import pickle
import numpy as np

class User(list):
    def __init__(self, name):
        self.name = name
        self.best = 100
    def __eq__(self, other):
        return not self<other and not other<self
    def __ne__(self, other):
        return self<other or other<self
    def __gt__(self, other):
        return other<self
    def __ge__(self, other):
        return not self<other
    def __le__(self, other):
        return not other<self
    def __lt__(self, other):
        return self.best<other.best
        
userDict = pickle.load(open('leaderboard.pk', 'rb'))

userRank = {}

printResult=True
while(1):
    updatedUsers=[]
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'csrftoken=JFp5PrYQJ7DLp9fNnHl2Tvnwteg9LcP3'))
    f = opener.open("https://competitions.codalab.org/competitions/11711/results/21941/data")
    for line in f.readlines():
        line = line.rstrip()
        if(line == 'submission_pk,User,Score'):
            continue
        info = line.split(',')
        if(len(info) < 3):
            continue
        username = info[1]
        score = float(info[2].split(' ')[0])
        if(not username in userDict):
            userDict[username] = User(username)
        if(len(userDict[username])==0):
        	printResult=True
        	updatedUsers.append(username)
        	userDict[username].append(score)
        else:
        	if(userDict[username][-1] != score):
        		printResult=True
        		updatedUsers.append(username)
        		userDict[username].append(score)
    pickle.dump(userDict, open('leaderboard.pk', 'wb'))
    with open('leaderboard.csv', 'w') as csv:
        for user in userDict.values():
            csv.write(user.name+','+','.join(map(str,user))+'\n')
    for user in userDict.values():
        user.best = min(user)
    if(printResult):    	
	    print('\n')
	    print('----Leaderboard----')
	    for idx,user in enumerate(sorted(userDict.values())):
	    	change = ' '
	    	if(not user.name in userRank):
	    		change = '>'
	    		userRank[user.name] = idx
	    	else:
	    		oldRank = userRank[user.name]
	    		userRank[user.name] = idx
	    		if(oldRank > idx):
	    			change='+'
	    		elif(oldRank < idx):
	    			change='-'
	    	if(change == ' ' and user.name in updatedUsers):
	    		change = '.'
	    	print(str(idx+1)+': '+change+' '+user.name+'\t'+str(user.best)+'/'+str(np.mean(user))+'/'+str(np.std(user))+' ('+str(len(user))+')')
	    print('-------------------')
    printResult=False
    sleep(30)
