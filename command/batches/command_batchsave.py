from command.batches.command_batch import Command_Batch


class Command_Batchsave(Command_Batch):
    """
    save given batch commands to file
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Batchsave.__instance:
            Command_Batchsave.__instance = object.__new__(cls)
        return Command_Batchsave.__instance

    def execute(self, command):
        try:
            2 <= len(command) <= 3
        except:
            return "invalid num command arguments"
        try:
            command[1][0] == "@"
        except:
            return "batch name must start with '@'"
        # if no file name to save use the batch name
        if len(command) == 2:
            file_name = command[1].replace("@", "") + ".dnabatch"
        else:
            file_name = command[2]
        try:
            with open(file_name, "w") as file:
                file.write("\n".join(super().get_batch_data().get_batch_by_name(command[1].replace("@", ""))))
                return "batch saved in file"
        except FileNotFoundError:
            return "file not found"
