import random
print("______________________________________POKER GAME___________________________________________")
print()
a = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
b = ["spade","club","diamond","heart"]
result = ["royal flush","straight flush","four of a kind","full house","flush","straight","three of a kind","two pair","one pair","high card"]
result.reverse()
point = 10
joint = 10
rounds=1
while point!=0 and joint!=20:
    c=[[],[]]
    n=0
    d=[[],[]]
    e=[[],[]]
    n=0
    f= []
    g= []
    f1=[]
    print()
    while len(c[0])!=2:
        x= random.choice(a)
        y = random.choice(b)
        if (str(x)+"-"+str(y)) not in f:
            c[0].append(x)
            f.append(str(x)+"-"+str(y))
            c[1].append(y)
    while len(d[0])!=2:
       x= random.choice(a)
       y = random.choice(b)
       if (str(x)+"-"+str(y)) not in f:
            d[0].append(x)
            f.append(str(x)+"-"+str(y))
            d[1].append(y)
    while len(e[0])!=5:
       x= random.choice(a)
       y = random.choice(b)
       if (str(x)+"-"+str(y)) not in f:
            e[0].append(x)
            f.append(str(x)+"-"+str(y))
            e[1].append(y)
    print(f[0]+" "+"and"+" "+f[1]+" "+"are your cards","","your points is- {}".format(point),sep="\n")
    inpu = 0
    while inpu<=point and inpu<=joint:
        inpu = int(input("enter your bet : "))
        print("______________________________________________________________________________")
        if inpu<=point and inpu<=joint:
            break
        else:
            print("place proper bet fuckface")
    print("\n")
    print("computer cards are",f[2],f[3])
    print("_______________________________________________________________________________")
        
    n=0
    k=0
    count1=0
    num = [0,0]
    count2 =0
    num2 = [0,0]
    index1 = [a.index(c[0][0]),a.index(c[0][1])]
    index2 = [a.index(d[0][0]),a.index(d[0][1])]
    max1 = 1
    maxindex1=-1
    maxindex2=-1
    while n!=2:
        x=c[0]+e[0]
        if x.count(c[0][n])>1:
            count1=count1+x.count(c[0][n])
            num[n]=1
            if a.index(c[0][n])>maxindex1:
                       maxindex1=a.index(c[0][n])
        y=d[0]+e[0]
        if y.count(d[0][n])>1:
            count2=count2+y.count(d[0][n])
            num2[n]=1
            if maxindex2<a.index(d[0][n]):
                                 maxindex2=a.index(d[0][n])
        n=n+1
        if c[0][0]==c[0][1]:
            count1 = 0
            count1= count1+x.count(c[0][0])
        if d[0][0]==d[0][1]:
            count2 = 0
            count2= count2+x.count(c[0][0])
    hush=1
    print()
    while hush!="s":
        hush =input("enter s to see the cards - ")
    print("the 5 cards are")
    print()
    for i in range(4,len(f)):
        print(f[i],end=" , " )
    print()
    print("_______________________________________________")
    for i in e[0]:
        if (i not  in c[0]) and (i not in d[0]):
            if e[0].count(i)>max1:
                max1 = e[0].count(i)
    if max1==1:
        max1=0


    if count1>count2:
        count1= count1 + max1
    elif count1==count2:
        if maxindex1>maxindex2:
            count1=count1+max1
        else:
            count2 = count2+max1
    else:
         count2 = count2+max1
    


    for i in range(0,3):
        if (count1==count2)and count1//2==i:
            if maxindex1>maxindex2:
                print("the winner is player")
                print(result[i])
                point = point+inpu
                joint = joint-inpu
            else:
                print("the winner is computer")
                print(result[i])
                point = point-inpu
                joint = joint+inpu
                
        elif (count1>count2) and count1//2==i:
            print("the winner is player")
            print(result[i])
            point = point+inpu
            joint = joint-inpu
        elif count1<count2 and count2//2==i:
            print("the winner is computer")
            print(result[i])
            point = point-inpu
            joint = joint+inpu
    print("your points is","-",point)
    print()
    print("computer point is","-",joint)
    print("____________________________________________________________________________")
    print()
    print()
    rounds = rounds+1
    if joint ==20:
        print()
        print("______________game over__________________YOU LOSE________________________")
        break
    elif point==20:
        print()
        print("_____________________YOU WON_________________________________")
        break
    hush=1
    while hush!="s":
        hush =input("enter s for next round -: ")
    print("______________________________ROUND",rounds,"_____________________________")
