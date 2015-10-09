import fileinput

outfile = open("mushroom_monster_out.txt","w")

x=1
infile = fileinput.input()
#skip number of testcases
infile.readline()
for line in infile:
 y,z = 0,0
 npoints = int(line)
 pl = map(int,infile.readline().split())
 diffs = [pl[i]-pl[i+1] for i in xrange(npoints-1)]
 rmax = max(max(diffs),0)
 y = sum([max(d,0) for d in diffs])
 z = sum([min(p,rmax) for p in pl[:-1]])
 outfile.write("Case #%d: %d %d" % (x,y,z)+"\n")
 x+=1
