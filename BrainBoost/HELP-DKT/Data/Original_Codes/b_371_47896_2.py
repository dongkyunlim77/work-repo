
guests = ['Zhang san','Li si','Wang wu','Zhao liu']
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests.append('Hu qi')
print(guests)
guests.insert(1,'Hu qi')
print(guests)
guest[2]='Wang shi'
print(guests)
del guests[0]
print(guests)
guests.remove('Zhang san')
print(guests)
