# Functions are cool
def power(num_1, num_2):
    '''
    Power is the name of our function
    You can name it anything you like
    but it must relate to what you want to return
    Here our function will return num_1** num_2
    num_1 and num_2 are the parameters were you
    pass in and then your function will manipulate
    to get the result
    >>> power(2,3)
    8
    >>> power(5,3)
    125
    '''
    return num_1 ** num_2


# if you want to call a function just
# type in the functions name and you'll get
# the function working for example: power(2,3)
print(power(2, 3))

# Slicing
# recall list's
people_who_are_invited = ['joe', 'andy', 'frankie', 'bobby', 'anthony', 'marcy', 'michele', 'manson', 'johnson']
# who is invited in my party
# there are three people that are not invited in my list
# andy , anthony and michele
# due to how poorly they did in last class
# but somehow they sneak off my bodyguards and put them self in the list
# How Do I Boot them off my party
for people in people_who_are_invited:
    # find where andy,anthony and michele
    if people == 'andy':
        index_1 = people_who_are_invited.index(people)
    elif people == 'anthony':
        index_2 = people_who_are_invited.index(people)
    elif people == 'michele':
        index_3 = people_who_are_invited.index(people)
# get out
andy = people_who_are_invited.pop(index_1)
anthony = people_who_are_invited.pop(index_2-1)
michele = people_who_are_invited.pop(index_3-2)
print(people_who_are_invited)
# what if I want to reverse my list
print(people_who_are_invited[::-1])
# what if I don't have enough booze
# and only the first three are invited
print(people_who_are_invited[:3])
# what if I want the last three
print(people_who_are_invited[3:])
# TODO: give a hard homework to andy, anthony and michele

