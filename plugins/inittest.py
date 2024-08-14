from lib.decorator import shell_command


class PlugInfo:  # DO NOT REMOVE
    def __init__(self, shell_instance):  # DO NOT REMOVE
        self.shell_instance = shell_instance

    @staticmethod
    def SNKInit():
        return {
            "name": "PluginName",  # Add your plugin name here
            "vendor": "PluginAuthor",  # Add yourself here :)
            "version": "PluginVersion",  # Add your version by using ""
            "description": "PluginDescription"  # Add your plugin's description here
        }


class ShellIntegrations:
    @shell_command
    def do_test(self, arg):
        print("hi!")
