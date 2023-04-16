class Archive:
    row_list = None
    books_list = None

    def __new__(cls, row: int, book: str):
        """
        This class can save previous values of early created classes
        :param row: the row of book
        :param book: the book
        """
        instance = super().__new__(cls)

        if cls.row_list is None and cls.books_list is None:
            cls.row_list = []
            cls.books_list = []
            instance.row = row
            instance.book = book
            cls.row_list.append(instance.row)
            cls.books_list.append(instance.book)
        else:
            instance.row = row
            instance.book = book
            cls.row_list.append(instance.row)
            cls.books_list.append(instance.book)
        return instance

    # def __str__(self):
    #     return f'{self.row} {self.book}'

    def __repr__(self):
        return f'Archive(row={self.row}, book={self.book})'


a1 = Archive(1, "asd")
print(a1)
a2 = Archive(2, 'dfg')
print(a2.row_list)
print(a2.books_list)
