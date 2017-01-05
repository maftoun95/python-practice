def a():
    global tester
    tester = 'setting a global from within a functions scope'

def b():
    tester = 'same name, local scope'

def c():
    print(tester) #since there is no variable tester in c, the global is checked


a()#tester is now set with as a global 
print(tester)
b()#tester is set as a local var but since its value is not printed,
#we wont get to see that value it was set to
print(tester)#this call will return the same value as the previous call
tester = 52#resetting the value of tester
c()#this will print testers new value
print(tester)#same
a()
print(tester)#back to the first value


'''
a variable will either always be global or always be local. There’s no way
that the code in a function can use a local variable named eggs and then
later in that same function use the global eggs variable.

If you ever want to modify the value stored in a global variable from in
a function, you must use a global statement on that variable.
'''
