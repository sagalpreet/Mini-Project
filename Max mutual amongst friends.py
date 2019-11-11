def bestmutual(org,l):   # l is list of original friends, org is person for whom we are finding
    d={}
    c=0
    ll=set(l)
    for i range(len(l)):
        f=open(l[i])
        s=f.readlines()
        for j in range(4,len(s)): # Moving from 4th line to bottom in a friend's file
            x=s[j] # friend's friend
            if(x==org or (x in d) or (x in l)):
                continue
            else:
                ff=open(x)
                fr=set(ff.readlines().split()[4:])
                c=fr.intersection(ll)
                d.update({x:c})

                

    v=list(d.values()) # taking values from dictionary
    for i in range(10): # top 10
        print(d[v.index(max(v))])
        v.remove(max(v))

    #            for k in range(len(l)):  # checking how many friends have x in common
     #               if(i!=k):
      #                  ff=open(l[i])
       #                 if(ff.find(x)==1):
        #                    c+=1
         #       d.update({x:c})
          #      c=0
