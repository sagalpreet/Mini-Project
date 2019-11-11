friend={}

def comp(a,b):
    f1=open(a+'.txt','r')
    f2=open(b+'.txt','r')
    s1=((f1.readlines()))
    s2=((f2.readlines()))
    k=0
    if s1[0]==s2[0] or s1[1]==s2[1]:
        k+=1
    if s1[2]==s2[2]:
        k+=2
    if s1[2]==s2[2]:
        k-=1
    f1.close()
    f2.close()
    f1=open(a+'.txt','r')
    f2=open(b+'.txt','r')
    s1=set(((f1.readlines()))[4:])
    s2=set((f2.readlines())[4:])
    s=s1&s2
    l=3*len(s)
    marks=k+l
    friend[b]=marks

    
base=[]
a=input()
f=open(a+'.txt')
original=((f.readlines()))[4:]
for i in range(4039):
    if(str(i)+'.txt' in original or str(i)==a):
       continue
    else:
        base.append(str(i))

for i in base:
    comp(a,i)

marklist=list(friend.values())
keylist=list(friend.keys())
for i in range(len(marklist)):
    print(keylist[marklist.index(max(marklist))])
    keylist.remove(marklist.index(max(marklist)))
    marklist.remove(max(marklist))
f.close()
