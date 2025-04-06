
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['zhang san','li si','wang wu','hu qi','liu ba']
guests.append('Hu qi')
del guests[0]
guests[2]='Wang shi'
print(guests)
 
