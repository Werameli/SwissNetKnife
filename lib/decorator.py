def shell_command(func):
    # Pretty basic function, but I wanted to make it separate file to add more custom decorators later
    func._is_shell_command = True
    return func