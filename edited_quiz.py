data = {
    'easy': {
        'sentence': "Water exists in __1__ states. Water in the ocean would "
                     "be a __2__. If water is frozen then it becomes a __3__. "
                     "When water boils it turns into a __4__.",
        'answers': ['three', 'liquid', 'solid', 'gas'],
        'attempts': 3
    },
    'medium': {
        'sentence': "Space is known as the __1__ frontier. Did you know "
                    "that the __2__ was once part of Earth? Harry Kerry "
                    "once said, If the moon was made of __3__ would you "
                    "eat it? The __4__ that astronauts have left on the "
                    "moon will be there for 100,000,000 years.",
        'answers': ['final', 'moon', 'rib', 'footprints'],
        'attempts': 2
    },

    'hard': {
        'sentence': "The closest star to earth  besides the sun is __1__. That "
                    "star is 4.2 __2__ away. It would take approximatley 500,000 "
                    "earth __3__ to travel to __1__. Scientific research states "
                    "that __1__ is located in the __4__ zone, which means it "
                    "could support life",
        'answers': ["alpha centauri", "light years", "years", "habitable"],
        'attempts': 1
    }
}


def select_level():
    while True:
        level = raw_input("Choose one level: ").lower()
        if level in data:
            sentence = data[level]['sentence']
            answers = data[level]['answers']
            attempts = data[level]['attempts']
            play(sentence, answers, attempts)
        print("Wrong level! Try again!")


def play(sentence, answers, attempts):
    index = 0
    while attempts >= 0 and index < len(answers):
        blank = '__' + str(index + 1) + '__'
        print(sentence)
        answer = raw_input('Answer to {}?'.format(blank))
        if answer == answers[index]:
            sentence = sentence.replace(blank, answer)
            index += 1
            if index == len(answers):
                print(sentence)
        else:
            attempts -= 1
            print("You have {} lives left.".format(attempts))

select_level()