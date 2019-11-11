def bestmutual(org,l):   # l is list of original friends, org is person for whom we are finding

    c=0
    ll=set(l) #set of friends of org
    for i range(len(l)):
        f1=open(l[i])
        s1=f1.readlines()
        for j in range(4,len(s1)): # Moving from 4th line to bottom in a friend's file
            x=s1[j] # friend's friend
            if(x==org or (x in d) or (x in l)):
                continue
            else:
                ff=open(x)
                fr=set(ff.readlines().split()[4:])  #creating a set of friends of x
                c=fr.intersection(ll) #intersection of both sets 
                d.update({x:len(c)})
                ff.close()

                
def printresults
    v=list(d.values()) # taking values from dictionary
    keylist=list(d.keys())
    for i in range(10): # top 10
        print(keylist[v.index(max(v))])
        keylist.pop([v.index(max(v))])
        v.remove(max(v))
        
a=input()
a+='.txt'
f= open(a)
s=f.readlines().split()[4:]  
d={}
bestmutual(a,s)






    #            for k in range(len(l)):  # checking how many friends have x in common
    #               if(i!=k):
    #                  ff=open(l[i])
    #                 if(ff.find(x)==1):
    #                    c+=1
    #            d.update({x:c})
    #            c=0

    
