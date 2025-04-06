
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
deleted_guset=[]
del guests[-1]
deleted_guset.append('hu ba')
guests.insert(2,'hu ba')
del guests[1]
print(deleted_guset)
print(guests)
