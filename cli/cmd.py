from cli.cli import CLI
from command.invoker import Invoker


class CMD(CLI):
    """
    inherit from CLI, Conducts with the user entering the commands
    """
    def __init__(self):
        super().__init__("> cmd >>>")
        self.__invoker = Invoker()

    def run(self):
        while True:
            command = input(super().get_prompt())
            command = command.strip().split()
            result = self.__invoker.run_command(command)
            # when confirm quit
            if result == "quit":
                print("Thank you for using Dnalanyzer.\nGoodbye!")
                break
            if result != None:
                print(result)
