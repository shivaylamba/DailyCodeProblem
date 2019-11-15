t=int(input())
while(t):
 s,z=int(input()),input()
 m,c,a,t=1,1,z[0],t-1
 for i in range(1,s):
  c=c+1if z[i]==z[i-1]else 1
  if c==m:a+=z[i]
  (m,a)=(c,z[i])if c>m else(m,a)
 print(m,''.join(sorted(set(a))))
