
guests = ['Zhang san','Li si','Wang wu','Zhao liu']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	

guests.pop(0)
guest[1]='Wang shi '
print(guests)
