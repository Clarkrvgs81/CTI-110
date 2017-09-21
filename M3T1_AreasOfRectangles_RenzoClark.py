# CTI-110
# M3T1-Areas of Rectangles
# Renzo Clark
# 9/21/17



length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

area1 = width1 * length1
area2 = width2 * length2


if area1 > area2:
    print('Rectangle 1 has the greater area.')
else:
    if area2 > area1:
        print('Rectangle 2 has the greater area.')
    else:
        print('Both have the same area.')
    
                    
