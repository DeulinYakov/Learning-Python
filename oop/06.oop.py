class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        return f'{self.text} {other.text}', self.votes_qty + other.votes_qty


first_comm = Comment('First comm')
first_comm.upvote()

sec_comm = Comment('sec comm')
sec_comm.upvote()

print( first_comm + sec_comm)