
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
A=guests.pop(-1)
guests.insert(2,A)
del guests[1]
print(A)
print(guests)
