import itertools
from collections import Counter

input_case = int(input("Enter number of test cases: "))
print()
print('======================================')


for q in range(input_case):
    tweetvalues=[]
    mylist=[]

    no_of_tweets_list = int(input("Enter number of tweets list: "))
    print("Enter twitter name with twitter_id separated by space:")
    for x in range(no_of_tweets_list):
        y=str(input('Enter '+str(x+1)+' value : '))
        tweetvalues.append(y)
    
    for x in range(len(tweetvalues)):
        x=tweetvalues[x].split(" ",1) #maxsplit
        #i=i+1
        mylist.append(x[0])

    #sorting in order 
    mylist.sort()
    #getting counts of unique value 
    cnt = Counter(mylist)
    #getting most number of tweets
    most_count=cnt.most_common()[0][1]
    #printing max tweets of user 
    for value, count in cnt.most_common():
        if(count==most_count):
            print('User with max number of tweets:')
            print(value, count)
            print('=============')

    



