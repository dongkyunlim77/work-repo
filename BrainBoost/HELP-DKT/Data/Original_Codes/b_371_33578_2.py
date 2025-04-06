
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests = ['zhang san', 'li si', 'wang wu', 'tan qi', 'hu ba']
del guest[4]
del guest[1]
guests.insert(1,'hu ba')
