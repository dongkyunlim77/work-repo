
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.pop()
deleted_guest=('Zhao liu')
guests.insert(2,deleted_guest)
guests.pop(1)
print(deleted_guest)
print(guests)

