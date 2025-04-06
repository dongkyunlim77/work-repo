
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
a=guests.pop(-1)
guests[1]=a
print(a)
print(guests)


