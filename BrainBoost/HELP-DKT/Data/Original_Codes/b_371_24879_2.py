
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
print(guests[4])
guests.insert(1,guests[4])
guests.pop(5)
guests.pop()
print(guests)
 
