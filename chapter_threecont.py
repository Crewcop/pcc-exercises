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

# 3-7
# inform people of the bad news
print("I am sorry to all guests, the desk has been broken," +
" we are only sitting 2 guests.\n")

# initial variable for length of list
guest_list_length = len(guest_list)

# pop command each person out of the list print them a message
for guest in guest_list:
	while guest_list_length > 2:
		popped_guest = guest_list.pop()
		print("Sorry " + popped_guest +
		", you cannot come to the dinner.\n")
		guest_list_length = len(guest_list)

# Send invitations out
for guest in guest_list:
    message = "Please come to my dinner " + guest.title() + ".\n"
    print(message)

#removing the last 2 people form the list using del command
print(guest_list)
del guest_list[:]
print(guest_list)
