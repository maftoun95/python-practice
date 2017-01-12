import random
#Because we want to use the random number generator
def magic8Ball():
    messages = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful',
        'Dont be such a wowzer']
    #Messages from the magic 8 ball
    print('Ask me anything.... I shall answer with unmatched certainty and clarity')
    #Bald faced lie
    litterallyNothing = input()
    #Offer the illusion of interactivity
    print(messages[random.randint(0, len(messages) - 1)])
    #Here, have an answer. Palm reading sold seperately
magic8Ball()
