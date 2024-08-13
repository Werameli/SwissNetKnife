def shell_command(func):
    func._is_shell_command = True
    return func