
guests = []
while True:
    try:
        guest = input()
        guests.append(guest)
    except:
        break

    
deleted_obj=guests.pop(-1)
print(deleted_obj)
print(guests)
