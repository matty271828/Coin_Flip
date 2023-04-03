def coin_flip():
    
    while True:
        try:
            numb = int(input("How many times would you like to flip: ?"))
        except ValueError:
            print("Sorry, choose an integer!")
        else:
            break
    
    return numb
       
 def the_flip(numb):
    
    import random
    
    total_tails = 0
    total_heads = 0
    
    for n in range(0,numb):
        if random.randint(0, 1) == 0:
            print('Heads')
            total_heads += 1
        else:
            print('Tails')
            total_tails += 1
    
    print('The number of tails is: ' + str(total_tails))
    print('The number of heads is: ' + str(total_heads))
        
 def main():
     while True:

        # opening statement
        print('Hi there, welcome to coin flip!')
        game_on = True

        while game_on:

            numb = coin_flip()

            the_flip(numb)

            break

        new_game = input('Would you like to flip again?: Y/N')

        if new_game[0].upper() == 'Y':
            game_on = True
            continue
        elif new_game[0].upper() != 'Y':
            print('Thanks for flipping!')
            break

if __name__ == "__main__":
    main();



