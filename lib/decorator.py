def shell_command(func):
    func._is_shell_command = True
    return func

def shell_remover(func):
    def wrapper(self, *args, **kwargs):
        self.__class__.commands_to_remove.append(func.__name__)
        return func(self, *args, **kwargs)
    return wrapper