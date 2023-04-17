class CheckName:
    def __init__(self, is_title, is_letters):
        self.is_title = is_title
        self.is_letters = is_letters

    def __set_name__(self, owner, name):
        self.obj_name = '_' + name

    def __set__(self, instance, value):
        if self.is_title(value) and self.is_letters(value):
            setattr(instance, self.obj_name, value)
        else:
            raise ValueError(f'Wrong {value}')

