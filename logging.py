from math import atan,pi
import fileinput
infile  = fileinput.input()
infile.readline()
outfile = open("logging_out.txt","w") 

def tan_theta(p,q):
 dx = q[0]-p[0]
 dy = q[1]-p[1]
 if not dx return 

i = 1
for line in infile.readline():
 npoints = int(line)
 squirrel_arr = [npoints]*npoints #initially all the trees must be cut down 
 p_arr = []
 for j in xrange(npoints):
  x,y = map(int,infile.readline().split())
  p_arr.append((x,y,j)) #keep track of which squirrel corresponds to what point
 
 p_arr = sorted(p_arr)
 start = p_arr[0]
 curr = start
 next = None
 while True:
  
  if next == start:
   break 
  curr = next
  
  
 
 break
