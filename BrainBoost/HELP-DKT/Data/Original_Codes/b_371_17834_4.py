
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
x='deleted_guest'
guests.append(guests)
guests.insert(x,2)
guests.pop(1)
print(x)
print(guests)
