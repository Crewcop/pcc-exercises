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
print("I hear Oliver is not coming, now Gus is coming.")
print(guest_list)
guest_list[2] = 'Gus'
print(guest_list)
