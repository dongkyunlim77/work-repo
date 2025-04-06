
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
x=guests[-1]
guests. pop()
guests. insert(2,x)
guests.pop(1)
print(x)
print(guests)
