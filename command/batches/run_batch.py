from command.batches.command_batch import Command_Batch
from command.invoker import Invoker


class Run_Batch_Command(Command_Batch):
    """
    run batch command after command and shoe result
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Run_Batch_Command.__instance:
            Run_Batch_Command.__instance = object.__new__(cls)
        return Run_Batch_Command.__instance

    def execute(self, command):
        try:
            len(command) == 2
        except:
            return "command run batch not valid"
        invoker = Invoker()
        res = []
        # get batch commands from data and run one by one
        try:
            batch_commands = super().get_batch_data().get_batch_by_name(command[1].replace('@', ''))
        except KeyError:
            return "batch name not exist"
        for command in batch_commands:
            res.append(invoker.run_command(command.strip().split()))
        return "\n".join(res)
