
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.pop(-1)
d=list.pop()
guests.insert(2,d)
guests.pop(1)
print(d)
print(guests)

