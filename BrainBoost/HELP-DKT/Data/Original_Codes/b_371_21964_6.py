
guests = []
while True:
	try:
		guest = input()
		guests.append(guest)
	except:
		break

	
guests=['zhang san','li si','wang wu','tan qi','hu ba']
deleted_obj=guests.pop()
guests[1]=deleted_obj
print(deleted_obj)
print(guests) 
