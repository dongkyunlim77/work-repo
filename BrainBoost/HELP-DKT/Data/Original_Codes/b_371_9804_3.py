
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guset=0
del guests[-1]
deleted_guset='hu ba'
guests.insert(2,'hu ba')
del guests[1]
print(deleted_guset)
print(guests)
