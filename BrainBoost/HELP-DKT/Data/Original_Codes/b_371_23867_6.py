
guests = ['Li si','Wang shi','Zhao liu','Hu qi']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guest =guests[-1]
guests.pop(-1)
guests.insert(2,deleted_guest)
guests.pop(1)
print(deleted_guest)
print(guests)

 
