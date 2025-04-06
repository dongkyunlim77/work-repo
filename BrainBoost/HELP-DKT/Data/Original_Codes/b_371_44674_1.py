
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append("Hu qi")
guests.remove("Zhang san")
guests.remove("Wang wu")
guests.insert(1,"Wang shi")
 
