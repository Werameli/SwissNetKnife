import lib.globalplaceholders as gph
from lib.decorator import shell_command, shell_remover

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
        pass

    def cleanup(self): # DO NOT REMOVE
        shell_integrations_class = getattr(self, 'ShellIntegrations', None)
        if shell_integrations_class:
            commands_to_remove = shell_integrations_class.commands_to_remove
            for command_name in commands_to_remove:
                if hasattr(self.shell_instance.__class__, command_name):
                    delattr(self.shell_instance.__class__, command_name)
                    print(f"Removed command: {command_name}")
        print(f"{self.SNKInit()['name']} cleaned up.")

class ShellIntegrations: # Add your command which you wanted to type in SNK's Shell here
    commands_to_remove = []
    @shell_command
    @shell_remover
    def do_test(self, arg):
        print("hi!")