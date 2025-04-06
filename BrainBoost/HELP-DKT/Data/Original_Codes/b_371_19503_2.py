
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
n=len(my_menu)
print(guests[0:n:3])
print(guests[-3:])

