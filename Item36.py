# -*- coding: cp1252 -*-
# Python 2.7.13

# Author: Nicholas Hardy

# Tech Academy Python Course, Item 36

def start(siblings=''):

    # REQ 1
    sibling_num = 0
    # REQ 2,3
    n_hardy = ['Nicholas','Hardy',5,float(11.5),185.5]

    son = ['Lincoln',13]

    parents = ('Melanie','Jeff')

    siblings = ('Rachel','Mylene','Sam','Danielle','Kellie',\
                'Adam','Vince')
    
    print('SUBJECT:')
    # REQ 4
    print('First Name: {}'.format(n_hardy[0]))
    print('Last Name: {}'.format(n_hardy[1]))
    print('Height: {} ft {} in'.format(n_hardy[2],n_hardy[3]))
    print('Weight: {} lbs'.format(n_hardy[4]))

    print('\nCHILDREN:')
    print('{}, {}'.format(son[0],son[1]))

    print('\nPARENTS:')
    # REQ 9,11
    for x in (parents):
        print(x)
    
    print('\nSIBLINGS:')
    # REQ 9,10
    for x in (siblings):
        print(x)
        sibling_num += 1
    # REQ 5
    name_num = len(n_hardy[0]) + len(n_hardy[1])
    nonsense = name_num * n_hardy[4] / sibling_num - 1
    print('\nSILLY STATS:')
    print('* Subject has a total of {} letters in their first and last name'\
          .format(name_num))
    if name_num == 13:
        print('-Spooky!')
    print("* (Total number of letters in subject's name) * (his weight) / (number of siblings) - 1 = " + str(nonsense))
    #REQ 13
    siblings = (polsky(siblings))
    for x in (siblings):
        print(x)
#REQ 12
def polsky(siblings):
    print("\nHow would you like to affect the sibling names?")
    print("1. Lower case")
    print("2. Upper case")
    print("3. Swap case")
    stop = True
    #REQ 8
    while stop:
        choice = raw_input("Choice: ")
        #REQ 6,7
        if choice == '1' and 10%2 == 0:
            siblings = [item.lower() for item in siblings]
            stop = False
        elif choice == '2' or choice == 'two':
            siblings = [item.upper() for item in siblings]
            stop = False
        elif choice == '3' and choice not in ('1','2'):
            siblings = [item.swapcase() for item in siblings]
            stop = False
        else:
            print('Choose 1, 2, or 3')

    return siblings      
    
        
        
if __name__ == '__main__':
    start()
