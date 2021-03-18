from itertools import permutations

def immright(h1,h2):
    return h1 - h2 == 1

def nextto (h1,h2):
    return h2 - h1 == 1 or h1 - h2 == 1

def zebra_puzzle():    
    houses = [First,_,Middle,_,_] = [1,2,3,4,5]
    orderings = list(permutations(houses)) #1
    #print(list(orderings))
    return next([Water,Zebra]
                for(English, Spaniard, Ukranian, Norwegian, Japanese) in orderings
                if Norwegian is First #10
                for(Red, Green, Ivory, Yellow, Blue) in orderings
                if English is Red #2
                if nextto(Norwegian, Blue)#15
                if immright(Green, Ivory) #6
                for(Milk, Oj, Tea, Coffee, Water) in orderings
                if Coffee is Green #4
                if Ukranian is Tea #5
                if Milk is Middle #9
                for(Dog, Zebra, Snails, Horse, Fox) in orderings
                if Spaniard is Dog #3
                for(OldGold, Kools, Chesterfield, LucyStrike, Parliaments) in orderings
                if OldGold is Snails #7
                if Kools is Yellow #8
                if nextto(Chesterfield, Fox) #11
                if nextto(Kools, Horse)#12
                if LucyStrike is Oj #13
                if Japanese is Parliaments #14
                )
print(zebra_puzzle())
def zebra_puzzle1():    
    houses = [First,_,Middle,_,_] = [1,2,3,4,5]
    orderings = list(permutations(houses)) #1
    #print(list(orderings))
    return next((Water,Zebra)
                for(Red, Green, Ivory, Yellow, Blue) in orderings
                if immright(Green, Ivory) #6
                for(English, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if English is Red #2
                if Norwegian is First #10
                if nextto(Norwegian, Blue)#15
                for(Coffee, Tea, Milk, Oj, Water) in orderings
                if Coffee is Green #4
                if Ukranian is Tea #5
                if Milk is Middle #9
                for(OldGold, Kools, Chesterfield, LucyStrike, Parliaments) in orderings
                if Kools is Yellow #8
                if LucyStrike is Oj #13
                if Japanese is Parliaments #14
                for(Dog, Snails, Fox, Horse, Zebra) in orderings
                if Spaniard is Dog #3
                if OldGold is Snails #7
                if nextto(Chesterfield, Fox) #11
                if nextto(Kools, Horse)#12
               )
    
print(zebra_puzzle1())
