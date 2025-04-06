
guests = ['Zhang san','Li si','Wang wu','Zhao liu']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guests=guests.pop()
guests.insert(2,deleted_guest) 
guests.insert(3,deleted_obj)
del guests[2]
print(guests)
