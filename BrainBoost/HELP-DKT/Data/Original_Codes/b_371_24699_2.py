
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['zhang san','li si','wang wu']
guests.append('tan qi')

guests[1]='hu ba'
print('hu ba')
print(guests)
 
