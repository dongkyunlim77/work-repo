
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
x=guests.pop(guests.index())
guests.insert(2,deleted_guest)
guests.pop(1)
print(x)
print(guests)
 
