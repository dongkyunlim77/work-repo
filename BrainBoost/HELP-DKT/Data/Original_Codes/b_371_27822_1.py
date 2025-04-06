guest=['Zhang san','Li si','Wang wu','Zhao liu']
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest=guests[-1]
guests.pop()
guest
