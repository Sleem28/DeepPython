class CheckGrade:
    def __init__(self, dn_board, up_board):
        self.dn_board = dn_board
        self.up_board = up_board

    def __set_name__(self, owner, name):
        self.obj_name = '_' + name

    def __set__(self, instance, value):
        if value >= self.dn_board and value <= self.up_board:
            setattr(instance, self.obj_name, value)
        else:
            raise ValueError(f'Wrong {value}. The value has got more or equals {self.dn_board}'
                             f' and less or equals {self.up_board}.')

