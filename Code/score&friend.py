friend={}
def comp(a,b):
    f1=open(a+'.txt','r')
    f2=open(b+'.txt','r')
    s1=((f1.readlines()).split())[4:]
    s2=((f2.readlines()).split())[4:]
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
    s1=set(((f1.readlines()).split())[4:])
    s2=set((f2.readlines()).split()[4:])    
    s=s1&s2
    l=3*len(s)
    marks=k+l
    friend[b]=marks
    
a=input()
