from command.management_commands.management_commands import Management_Commands
from cli.confirm import Confirm


class Command_Del(Management_Commands):
    """
    delete given seq from data
    """
    __confirm = Confirm()
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Del.__instance:
            Command_Del.__instance = object.__new__(cls)
        return Command_Del.__instance

    def execute(self, command):
        super().init_command(command)
        error = super().check_command(command)
        if error: return error
        if len(command) == 3:
            return "command del not valid"
        dna_deleted = super().get_seq_to_manage(command)
        if not dna_deleted:
            return "seq not in data"
        result = self.__confirm.run(
            f"Do you really want to delete {dna_deleted.get_dna_name()}: {dna_deleted.get_dna()} ? Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
        if result:
            try:
                super().get_dna_data().delete_sequence(dna_deleted)
            except ValueError:
                return "seq to delete not valid"
            return f"Deleted [{dna_deleted.get_dna_id()}] {dna_deleted.get_dna_name()}: {dna_deleted.get_dna()}"
        return "cancel delete"
