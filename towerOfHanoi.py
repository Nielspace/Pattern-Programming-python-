"""the link to the concept is given below 
   https://en.wikipedia.org/wiki/Tower_of_Hanoi """


def TowerOfHanoi(n , rodA, rodB, rodC): 
    if n == 1: 
        print ("Move disk 1 from rod",rodA,"to rod",rodB )
        return
    TowerOfHanoi(n-1, rodA, rodC, rodB) 
    print ("Move disk",n,"from rod",rodA,"to rod",rodB )
    TowerOfHanoi(n-1, rodC, rodB, rodA) 


TowerOfHanoi(4, 'A','C', 'B')