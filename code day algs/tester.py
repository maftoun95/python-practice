def titleCase(str):
    final = ''
    
    arr = str.split()
    for word in arr:
        mod=''
        for first in word:
            
            if first == word[0]:
                mod+=first.upper()
            else:
                mod+=first
            
        final += mod+' '
    print(final)

titleCase('the one about the quick brown fox')
