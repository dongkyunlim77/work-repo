
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
del guests[1]
x=guests[1]
guests.insert(1,1)
print(x,guests)
