class Comment:
    total_coments = 0

    def __init__(self, text):
        self.text = text
        self.likes = 0

        Comment.total_coments += 1


first_comment = Comment('first comment')
print(Comment.total_coments)

second_comment = Comment('second')
print(Comment.total_coments)