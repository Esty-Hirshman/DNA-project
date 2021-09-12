from cli import Batch
from command.batches.command_batch import Command_Batch


class Create_Batch(Command_Batch):
    """
    create new batch, Receives command after command until 'end' is entered
    """
    __instance = None
    __batch = Batch()

    def __new__(cls, *args, **kwargs):
        if not Create_Batch.__instance:
            Create_Batch.__instance = object.__new__(cls)
        return Create_Batch.__instance

    def execute(self, command):
        try:
            len(command) == 2
        except:
            return "command batch not valid"
        # if batch name already used return error massage
        if super().get_batch_data().is_name_in(command[1]):
            return f"batch {command[1]} already exist"
        commands = self.__batch.run()
        super().get_batch_data().append_batch(command[1],commands)
