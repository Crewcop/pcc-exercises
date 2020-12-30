# 3-4
# guest list
guest_list = ['Liam',
'Noah',
'Oliver',
'William',
'Elijah',
'James',
'Benjamin',
'Lucas',
'Mason',
'Ethan',
'Alexander'
]

for guest in guest_list:
    message = "Please come to my dinner " + guest.title() + ".\n"
    print(message)

# 3-5
print("I hear Oliver is not coming, now Gus is coming.\n")
print(guest_list)
guest_list[2] = 'Gus'
print(guest_list)
print()

for guest in guest_list:
    message = "Please come to my dinner " + guest.title() + ".\n"
    print(message)

# 3-6
#add 3 more guests to the guest_list
print('We have 3 more spots free at the dining table.\n')
# start of list
guest_list.insert(0, 'Harry')
# middle of list
middle = int(len(guest_list)/2)
guest_list.insert(middle, 'Larry')
# end of list
guest_list.append('Barry')

for guest in guest_list:
    message = "Please come to my dinner " + guest.title() + ".\n"
    print(message)
