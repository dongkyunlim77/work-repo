
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
a=guests.pop()
guests.insert(2,a)
del guests[1]
print(a)
print(guests)
 
