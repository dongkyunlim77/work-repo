
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
y=guests[-1]
print(y)
guests[1]=y
guests.pop()
print(guests)
 
