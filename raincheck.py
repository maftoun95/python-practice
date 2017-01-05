def isRaining():
    print('Time to head out. Is it raining?')
    check = input()
    if check == 'yes':
        print('No big. Got an umbrella??')
        bumbershoot = input()
        if bumbershoot == 'yes':
            print('K, see you')
        elif bumbershoot == 'no':
            print('Wait for a while')
            print('.')
            print('..')
            print('...')
            print('Is it still raining?')
            still = input()
            if still == 'yes':
                print('Wait a little longer I guess...')
                print('.')
                print('..')
                print('...')
                print('....')
                print('.....')
                print('......')
                print('.......')
                print('........')
                print('.........')
    elif check == 'no':
        print('K, see you')
        
isRaining()
