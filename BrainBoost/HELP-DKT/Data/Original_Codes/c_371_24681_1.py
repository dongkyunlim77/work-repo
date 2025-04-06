
guests = []
for i in range(4):
    guest = input()
    guests.append(guest)
to_add = input()



guests.insert(2,to_add)
deleted_guest = guests.pop(1)
print(guests)
print(deleted_guest)

