def deletes(n,a):
	for i in a:
		if i==n :
			a.remove(n)
		print(a)
		break
deletes(40,[40,50,60,40,50,60,23,45])

import array
arr1=array.array('i',[15,20,25,78,50,87])

deletes(3,arr1)

