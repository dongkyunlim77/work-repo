
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guest=guests[-1]
guests.pop()
guests.insert(2,guest)
guest.pop(1)
print(guest)
print(guests)
