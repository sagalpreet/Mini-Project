friend={}

def arrange(l,d):
    if len(l)>0:
        k=int(d[l[-1]][0])
        a=[]
        b=[]
        for i in range(len(l)-1):
            if int(d[l[i]][0])<=k:
                a.append(l[i])
            elif int(d[l[i]][0])>=k:
                b.append(l[i])
        return arrange(a,d)+[l[-1]]+arrange(b,d)
    else:
        return []

def comp(a,b):
    f1=open(a,'r')
    f2=open(b,'r')
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
    f1=open(a,'r')
    f2=open(b,'r')
    s1=set(((f1.readlines()))[4:])
    s2=set((f2.readlines())[4:])
    s=s1&s2
    f1.close()
    f2.close()
    l=3*len(s)
    marks=k+l
    friend[b]=[marks,len(s)]

a=input()
f=open(a+'.txt')
original=((f.readlines()))[4:]
for i in original:
    g=open(i[:-1],'r')
    original_next=g.readlines()[4:]
    for j in original_next:
        if j not in original and j!=a+'.txt\n':
            comp(a+'.txt',j[:-1])
    g.close()
f.close()
all=[]
#sort
for i in friend:
    all.append(i)
all=arrange(all,friend)
for i in range(-1,-11,-1):
    try:
        print('You have',friend[(all[i])][1],'mutual friends with',all[i])   
    except:
        break
