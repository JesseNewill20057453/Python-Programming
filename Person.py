from postman import Postman
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
            print('Alice has delivered a letter to the Post Office')

        elif self.name == 'Bob':
            print('Alice has delivered a letter to the Post Office')
        else:
            print('ERROR')

    def read_letter(self):
        if letterReader == 'Alice':
            print('Alice read the letter')
        elif letterReader == 'Bob':
            print('Bob has read the letter')

    def encrypted(self):
        if letterWritter == 'Alice':
            print('Alice has encrypted the letter')
        elif letterWritter == 'Bob':
            print('Bob has encrypted the letter')
        else:
            print('ERROR')

    def decrypted(self):
        if letterWritter == 'Alice':
            print('Bob has decrypted the letter')
        elif letterWritter == 'Bob':
            print('Alice has decrypted the letter')
        else:
            print('ERROR')

letterWritter = input('Who is writing the letter: ')
if letterWritter == 'Alice':
    letterReader = 'Bob'
elif letterWritter == 'Bob':
    letterReader = 'Alice'
else:
    print('ERROR')

letterState = 'Encrypted'
postman = 'Charli'
p1 = Person(letterWritter)
p1.write_Letter()
p1.encrypted()
p1.deliver_Letter()
po1 = Postman.receivedLetter(postman)
po1 = Postman.pickedUp(postman)
po1 = Postman.deliveredLetter(postman)
p1.decrypted()
p1.read_letter()


