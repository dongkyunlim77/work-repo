
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guest=guest[-1]
guests.pop()
guests.pop(1)
guests.insert(1,'hu ba')
print(guest)
print(guests)
 
