import fileinput as fileinput
infile = fileinput.input()
infile.readline() #skip number of testcases
outfile = open("haircut_out.txt","w")

#number of custs served after mins minutes
def nserved(mins,arr):
 s = 0
 if not mins:
  return len(arr)
 for t in arr:
  s += (mins/t) + 1 #get ceiling
 return s

def prob(B,N,M):
 if N <=B:
  return N
 
 n = 1
 srv = nserved(1,M)
 while srv < N:
  n = 2*n
  srv = nserved(n,M)
 lsrv = nserved(n/2,M)
 up = n
 low = n/2
 while up-low > 1:
   mid = (up+low)/2
   tsrv = nserved(mid,M)
   if tsrv >= N:
     up,srv = mid,tsrv
   else:
     low,lsrv = mid,tsrv
 #now, you're served at up minutes
 #iterate over free barbers at up minutes, you get the srv-Nth one
 nfree = 1
 for pos,t in enumerate(M):
   if up%t == 0:
     if nfree == N-lsrv:
      return pos+1
     nfree += 1 
 
i=1
for line in infile:
 B,N = map(int,line.split())
 M = map(int,infile.readline().split())
 
 outfile.write("Case #%d: %d\n"%(i,prob(B,N,M)))   
 i +=1
