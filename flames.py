import sys
a=input('enter first person name:')
b=input('enter second person name:')
a=a.lower()
b=b.lower()
if len(a)==0 and len(b)==0:
    sys.stderr.write('enter atleast one word to proceed :(')
    sys.exit()
elif len(a)==0 or len(b)==0:
    sys.stderr.write('enter words in both inputs :(')
    sys.exit()
c=''
d=''
for i in a:
    if i=='.' or i==' ':
        continue
    else:
        c+=i
for i in b:
    if i=='.' or i==' ':
        continue
    else:
        d+=i
e=list(c)
f=list(d)
if len(e)==len(f):
    for i in range(len(e)):
        for j in range(len(e)):
            if e[i]==f[j]:
                e[i]='*'
                f[j]='*'
                break
else:
    for i in range(len(e)):
        for j in range(len(f)):
            if c[i]==d[j]:
                e[i]='*'
                f[j]='*'
                break
ori=''
for i in e:
    if i=='*':
        continue
    else:
        ori+=i
for i in f:
    if i=='*':
        continue
    else:
        ori+=i
ori=len(ori)
g='FLAMES'
go=0
while True:
    if len(g)==1:
        print(g)
        break
    for i in g:
        go+=1
        if go%ori==0:
            if g.index(i)==0:
                g=g[g.index(i)+1:]
                break
            elif g.index(i)==len(g)-1:
                g=g[:g.index(i)]
                break
            else:
                g=g[g.index(i)+1:]+g[:g.index(i)]
                break