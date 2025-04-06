
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guest1=guests.pop(-1)
guests.insert(2,guest1)
del guests[1]
print(guest1)
print(guests)
 
