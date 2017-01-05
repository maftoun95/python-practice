name = 'Dracula'
age = 4283
'''
once an elif runs, the rest are skipped. Even though age is > 2000,
only the grannie check will run. else will trigger only if all previous
stmts evaluate to flase
At most one if, elif, or else stmt will run
'''
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print("You aren't Alice, young gun.")
elif age > 100:
    print('You are not Alice, Gramps')
    '''
once an elif runs, the rest are skipped. Even though age is > 2000,
only the grannie check will run. else will trigger only if all previous
stmts evaluate to flase
At most one if, elif, or else stmt will run
'''
elif age >2000:
    print("Unlike you, Alice isn't an undead, imortal vampyr.")
    '''
It would also appear that indents matter in code as well.
when I pushed back the preceding comment opening to be flush
with these lines, I was given an invalid synthax error : (
'''
else:
    print("It would appear you are neither Alice or a vampire.")
