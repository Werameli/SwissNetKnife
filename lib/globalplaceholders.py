with open(".version", "r") as file:
    # Well, this just checks .version file to then later compare it to repo's one
    version = file.read()
    file.close()