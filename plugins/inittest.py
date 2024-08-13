import lib.globalplaceholders as gph
from lib.decorator import shell_command

class PlugInfo:
    def __init__(self, shell_instance):
        self.shell_instance = shell_instance

    @staticmethod
    def SNKInit():
        return {
            "name": "PluginExample",
            "vendor": "Werameli",
            "version": gph.version, # add your version by using ""
            "description": "Example plugin with simple functions and init function"
        }

    def init(self): # Unnecessary function
        print(f"{self.SNKInit()['name']} initialized.")


    @staticmethod
    def cleanup(cls, shell_instance): # Unnecessary function
        for command in cls.commands_to_remove:
            if hasattr(shell_instance.__class__, command):
                delattr(shell_instance.__class__, command)
                print(f"Removed command: {command}")

class ShellIntegrations:
    @shell_command
    def do_test(self, arg):
        print("hi!")