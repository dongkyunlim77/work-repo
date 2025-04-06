
guests = ['Zhang San','Li si','Wang wu','Zhao liu']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
guests.pop(0)
guests['Wang wu']= 'Wang shi'
print(guests)
