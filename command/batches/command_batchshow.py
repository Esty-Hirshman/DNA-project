from command.batches.command_batch import Command_Batch


class Command_Batchshow(Command_Batch):
    """
    shoe specific batch commands
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Batchshow.__instance:
            Command_Batchshow.__instance = object.__new__(cls)
        return Command_Batchshow.__instance

    def execute(self, command):
        try:
            len(command) == 2
        except:
            return "invalid num command arguments"
        try:
            command[1][0] == "@"
        except:
            return "batch name must start with '@'"
        return "\n".join(super().get_batch_data().get_batch_by_name(command[1].replace("@", '')))
