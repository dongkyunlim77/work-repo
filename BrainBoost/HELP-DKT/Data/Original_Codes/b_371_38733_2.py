
guests = ['Zhang san','Li si','Wang wu','hu qi' 'liu ba']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
delete_guest=guests.pop()
guests.insert(2,delete_guest)
guests.pop(1)
print(delete_guest)
print(guests)
