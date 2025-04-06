
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.remove(guest)
guests.insert(2,guest)
del guests[1] 


 
