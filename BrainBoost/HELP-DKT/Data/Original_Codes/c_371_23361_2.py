
guests = []
while True:
    try:
        guest = input()
        guests.append(guest)
    except:
        break

    
deleted_guest=guests.pop(-1)
guests[2]=deleted_guest
 
