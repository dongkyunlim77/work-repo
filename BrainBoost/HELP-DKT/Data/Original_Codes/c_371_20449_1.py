
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
dg=guests.pop(-1)
print(dg)
guests.insert(2,dg)
del guests[1]
print(guests)
