
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
daleted_guest=guests.pop()
guests.insert(2,daleted_guest)
guests.pop(1)
print(daleted_guest)
print(guests)

