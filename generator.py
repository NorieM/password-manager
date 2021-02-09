from random import choice, randint, shuffle


class Generate:

    def __init__(self):
        self.letters = list(map(chr, range(97, 123)))
        self.letters = self.letters + list(map(lambda ch: ch.upper(), self.letters))
        self.numbers = [str(i) for i in range(10)]
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate_password(self):
        password_letters = [choice(self.letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(self.symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(self.numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers

        shuffle(password_list)

        password = ''.join(password_list)

        return password
