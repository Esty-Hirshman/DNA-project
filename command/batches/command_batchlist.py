from command.batches.command_batch import Command_Batch


class Command_Batchlist(Command_Batch):
    """
    command to get all batches name
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Batchlist.__instance:
            Command_Batchlist.__instance = object.__new__(cls)
        return Command_Batchlist.__instance

    def execute(self, command):
        try:
            len(command) == 1
        except ValueError:
            return "invalid num arguments in batch list command"
        return " ".join(super().get_batch_data().get_all_batches())
