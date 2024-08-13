def SNKInit():
    return {
        "name": "PluginExample",
        "vendor": "Werameli",
        "version": "pre-Beta 1.1",
        "description": "Example plugin with simple functions and init function"
    }

def init():
    print(f"PluginExample has been initiated!")

def cleanup():
    print("PluginExample is cleaning up!")