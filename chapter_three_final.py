# 3-8
# list of locations
destinations = ['london', 'madrid', 'brisbane', 'sydney', 'melbourne']
print(destinations)

# print the list alphabetically without modifying it
print('\nHere is the sorted list : ')
print(sorted(destinations))

# print the original order
print('\nHere is the original list still :')
print(destinations)

# print the list in reverse alpha order
print('\nHere is the sorted list in reverse : ')
print(sorted(destinations, reverse=True))
print(destinations,'\n')

# use reverse to change the order
destinations.reverse()
print(destinations, '\n')

# reverse it back
destinations.reverse()
print(destinations, '\n')

# sort the list alphabetically permanently
destinations.sort()
print(destinations, '\n')

# use sort() to reverse the order
destinations.sort(reverse=True)
print(destinations, '\n')
