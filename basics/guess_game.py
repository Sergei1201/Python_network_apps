def newGame():
    guesses = []
    correctGuesses = 0
    questionNum = 1

    for key, value in questions.items():
        print(key)
        for i in options[questionNum - 1]:
            print(i)
        guess = input('Enter A, B, C or D ').upper()
        guesses.append(guess)
        correctGuesses += checkAnswer(questions.get(value), guess)
        questionNum += 1

    displayScores(correctGuesses, guesses)


def checkAnswer(answer, guess):
    if answer == guess:
        print('You are correct')
        return 1
    else:
        print('You are wrong')
        return 0


def displayScores(correctGuesses, guesses):
    print('Results')
    print('Answers: ', end='')
    for key, value in questions.items():
        print(value, end=' ')
    print()
    print('Guesses: ', end='')
    for i in guesses:
        print(i, end=' ')


def playAgain():
    pass


questions = {
    'Who created C++?': 'A',
    'Who created Python?': 'B',
    'Who created JavaScript?': 'C',
    'Who created PHP?': 'B'
}

options = [
    ['A. Danish specialist', 'B. Russian specialist',
        'C. British specialist', 'D. American specialist'],
    ['A. Danish specialist', 'B. Russian specialist',
        'C. British specialist', 'D. American specialist'],
    ['A. Danish specialist', 'B. Russian specialist',
        'C. British specialist', 'D. American specialist'],
    ['A. Danish specialist', 'B. Russian specialist',
        'C. British specialist', 'D. American specialist']
]

newGame()
