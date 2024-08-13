import lib.globalplaceholders as gph
from lib.decorator import shell_command

class PlugInfo: # DO NOT REMOVE
    def __init__(self, shell_instance): # DO NOT REMOVE
        self.shell_instance = shell_instance

    @staticmethod
    def SNKInit(): # NO NOT REMOVE
        return {
            "name": "PluginExample", # Add your plugin name here
            "vendor": "Werameli", # Add yourself here :)
            "version": gph.version, # Add your version by using ""
            "description": "Example plugin with simple functions" # Add your plugin's description here
        }

    def init(self): # DO NOT REMOVE
        print(f"{self.SNKInit()['name']} initialized.")


    @staticmethod
    def cleanup(cls, shell_instance): # DO NOT REMOVE
        for command in cls.commands_to_remove:
            if hasattr(shell_instance.__class__, command):
                delattr(shell_instance.__class__, command)
                print(f"Removed command: {command}")

class ShellIntegrations: # Add your command which you wanted to type in SNK's Shell here
    @shell_command
    def do_test(self, arg):
        print("hi!")