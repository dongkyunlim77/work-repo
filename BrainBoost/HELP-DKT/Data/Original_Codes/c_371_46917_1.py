
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
aaa=guests.pop(-1)
guests.insert(2,aaa)
del guests[1]
print(aaa)
print(guests)
 
