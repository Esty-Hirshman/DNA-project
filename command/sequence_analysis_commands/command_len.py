from command.command import Command


class Command_Len(Command):
    """
    get length of seq
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Len.__instance:
            Command_Len.__instance = object.__new__(cls)
        return Command_Len.__instance

    def execute(self, command):
        try:
            len(command) == 2
        except:
            return "command not valid"
        try:
            # must get seq_id
            command[1][0] == "#"
        except:
            return "command not valid, id must start with  '#'"
        dna = super().get_dna_data().get_sequence_by_id_or_name(command[1])
        if not dna:
            return "seq not found"
        return len(dna)
