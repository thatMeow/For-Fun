n=3
s1=','.join(['i'+str(i) for i in range(n)])
s2=''.join(["for i"+str(i)+" in xrange(10) " for i in range(n)])
code = "["+"("+s1+") "+s2 +"]"
print eval(code)
