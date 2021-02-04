name=list()
scores=list()
avg=0
def average(scores):
    total=0
    n=len(scores)
    for item in scores:
        total=total+item
    average=total/n
    return average
def highestscore(scores):
    highest=0
    n=len(scores)
    for i in range(n):
        if scores[i]>highest:
            highest=scores[i]
            highestname=name[i]
            person=list()
            person.append(highestname)
            person.append(highest)
            retern person 
def lowestscore(scores):
    lowest=100
    n=len(scores)
    for i in range(n):
        if scores[i]<lowest:
            lowest=scores[i]
            lowestname=name[i]
            person=list()
            person.append(lowestname)
            person.append(lowest)
            retern person 
n=input('how many people in this class?')
n=int(n)
for  i in range(n)