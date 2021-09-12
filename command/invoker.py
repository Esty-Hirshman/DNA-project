from command.factory import Factory


class Invoker:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Invoker.__instance:
            Invoker.__instance = object.__new__(cls)
        return Invoker.__instance

    def __init__(self):
        self.__factory = Factory()

    def run_command(self, command_to_execute):
        """
        get the command from factory and execute it
        :param command_to_execute
        """
        try:
            command_type = self.__factory.get_command_type(command_to_execute[0])
        except KeyError:
            return "command not valid"
        return command_type.execute(command_to_execute)


