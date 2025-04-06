
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deletedguest=guests[-1]
guests[1]=deletedguest
guests.pop()
print(deletedguest)
print(guests)
