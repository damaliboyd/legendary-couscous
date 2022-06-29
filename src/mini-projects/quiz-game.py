print('Welcome To The US Capitols Quiz')

will_playing = input('Do you want to play?[yes/no] ')

if will_playing.lower() != 'yes':
    print('Have a great day!')
    quit()

print('you are playing')

score = 0

questions = [
    'What is the capitol of Alaska? ',
    'What is the capitol of Texas? ',
    'What is the capitol of California? ',
    'What is the capitol of Montana? ',
    'What is the capitol of New Mexico? '
]

answers = [
    'juneau',
    'austin',
    'sacramento ',
    'helena',
    'santa fe'
]

for i in range(len(questions)):
    answer = input(questions[i])
    if answer.lower() == answers[i]:
        score = score + 1
        print("Correct!")
    else:
        print(f'Incorrect correct answer is {answers[i]}')

print(f'You got {score}/5 right')