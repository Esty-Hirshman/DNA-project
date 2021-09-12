import os

from command.batches.command_batch import Command_Batch


class Command_Batchload(Command_Batch):
    """
    read batch commands from file and insert them to batch data
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Batchload.__instance:
            Command_Batchload.__instance = object.__new__(cls)
        return Command_Batchload.__instance

    def execute(self, command):
        try:
            2 <= len(command) <= 3
        except:
            return "invalid num command arguments"
        try:
            with open(command[1], "r") as file:
                # if batch name was not send, use the file name
                if len(command) == 2:
                    batch_name = os.path.splitext(os.path.basename(command[1]))[0]
                else:
                    try:
                        command[2][0] == "@"
                    except:
                        return "batch name must start with '@'"
                    batch_name = command[2].replace("@", "")
                batch_data = file.readlines()
                batch_data = [i.replace('\n', '') for i in batch_data]
                super().get_batch_data().append_batch(batch_name, batch_data)
                return f"batch {batch_name} loaded"
        except FileNotFoundError:
            return "file not found"
