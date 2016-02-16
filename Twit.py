
import tweepy, time, sys, random
from random import randint
 
argfile = str("liners.txt")
 

 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY =  'qqFs1kWZOaglyVXtjoIfFKRk5'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'z5MxVamLA34IztvVg8kr2LUKiYU2fAhjRLGU35rOzH7W9Ky6kU'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '4913031806-BQmZqyEhFRiawcXwmfGiMuWgRc3rv0gm5j2O6wA'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'UpNdvblV9QuB3XCwzKt2n3EJxx4BuhhtDLeEzXPAK0Di7'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
while True:
    for line in f:
        curtime= time.strftime("%H:%M:%S")
        curdate= time.strftime("%x")
        api.update_status("{0}---{1}, {2}".format(curdate,curtime,line)) 
        TimeToSleep = randint(780,1200)
        time.sleep(TimeToSleep)#Tweet every 15 minutes