
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['Zhang san','Li si','Wang wu','Zhao liu']
deleted_guests = guests.pop(3)
guests.insert(2,deleted_guests)
del guests[1]
print(deleted_guests)
print(guests)

