
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['zhang san','li si','wang wu','tan qi','hu ba']
deleted_obj=guests.pop()
guests[2]='hu ba'
print(deleted_obj)
print(guests) 
