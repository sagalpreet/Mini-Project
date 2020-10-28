#this file is meant to create user files from source file downloaded from the snap stanford.
f=open('facebook_combined.txt','r',encoding='utf-8')
s=' '
while s!='':
  s=f.readline()
  if s=='':
    break
  l=s.split()
  l[0]=l[0]+'.txt'
  l[1]=l[1]+'.txt'
  g=open(l[0],'a+',encoding='utf-8')
  g.write(l[1]+'\n')
  g.close()
  g=open(l[1],'a+',encoding='utf-8')
  g.write(l[0]+'\n')
  g.close()