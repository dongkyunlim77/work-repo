
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deletd_guest=guests.pop(-1)
guests.insert(2,deletd_guest)
del guests[1]
print(deletd_guest)
print(guests)
