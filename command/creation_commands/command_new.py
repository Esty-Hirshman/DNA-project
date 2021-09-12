from command.creation_commands.creation_commands import Creation_commands


class Command_New(Creation_commands):
    """
    insert new seq to data
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_New.__instance:
            Command_New.__instance = object.__new__(cls)
        return Command_New.__instance

    def execute(self, command):
        command.append("o")
        super().init_command(command)
        error = super().check_command()
        if error: return error
        return super().execute()
