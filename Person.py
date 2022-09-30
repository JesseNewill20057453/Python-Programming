class Person:
    def __init__(self, name):
        self.name = name

    def write_Letter(self):
        if self.name == 'Alice':
            print('Alice is writing a letter to Bob')

        elif self.name == 'Bob':
            print('Bob is wrting a letter to Alice')

        else:
            print('ERROR')

    def deliver_Letter(self):
        if self.name == 'Alice':
            print('Alice has delivered a letter to Bob')
            letterboxEmpty = False
            if letterboxEmpty == False:
                print('The flag is up, Bob has a new letter!')
            else:
                print('The flag is down, Bob has no new message')

        elif self.name == 'Bob':
            print('Bob has dilivered a letter to Alice')
            letterboxEmpty = False
            if letterboxEmpty == False:
                print('The flag is up, Alice has a new letter!')
            else:
                print('The flag is down, Alice has no new message')
        else:
            print('ERROR')

    def read_letter(self):
        if letterReader == 'Alice':
            print('Alice read the letter')
        elif letterReader == 'Bob':
            print('Bob has read the letter')

letterWritter = input('Who is writing the letter: ')
if letterWritter == 'Alice':
    letterReader = 'Bob'
elif letterWritter == 'Bob':
    letterReader = 'Alice'
else:
    print('ERROR')

person1 = Person(letterWritter)
person1.write_Letter()
person1.deliver_Letter()
person1.read_letter()


