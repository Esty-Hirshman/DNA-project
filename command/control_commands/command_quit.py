from command import Command
from cli.confirm import Confirm


class Command_Quit(Command):
    """
    quit the cmd
    """
    __instance = None
    __confirm = Confirm()

    def __new__(cls, *args, **kwargs):
        if not Command_Quit.__instance:
            Command_Quit.__instance = object.__new__(cls)
        return Command_Quit.__instance

    def execute(self, command):
        try:
            command == ["quit"]
        except:
            return "quit command not valid"
        # get number of new sequences that was not saved in file
        num_new = super().get_dna_data().get_num_new_seq()
        # Gets the sequences number that changed after the last save to the file
        num_modified = super().get_dna_data().get_num_modified_seq()
        massage = f"There are {num_modified} modified and {num_new} new sequences," if (num_modified or num_new) else ""
        result = self.__confirm.run(f"{massage} Are you sure you want to quit?")
        if result:
            return "quit"
        return "quit canceled"
