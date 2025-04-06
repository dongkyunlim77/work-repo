
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

print(guest)
print(guests)
 
