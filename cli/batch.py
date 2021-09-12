from cli import CLI


class Batch(CLI):
    """
    class inherit from CLI to handle and get commands for batch
    """
    def __init__(self):
        super().__init__("> batch >>>")

    def run(self):
        command_to_add = ""
        batch_commands = []
        while command_to_add != "end":
            command_to_add = input(super().get_prompt())
            if command_to_add.split()[0] == "run":
                print("command run not valid in batch")
                continue
            if command_to_add != "end":
                batch_commands.append(command_to_add)
        return batch_commands



