
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
print(guests[len(guests)-1])
guests.insert(1,guests[4])
guests.pop()
guests.pop(2)
print(guests)
 
