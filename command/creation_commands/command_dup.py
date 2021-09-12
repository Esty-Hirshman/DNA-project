from command.command import Command


class Command_Dup(Command):
    """
    Duplicate given sequence
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Dup.__instance:
            Command_Dup.__instance = object.__new__(cls)
        return Command_Dup.__instance

    def execute(self, command):
        try:
            command[1][0] == '#' or command[1][0] == '@'
        except ValueError:
            return "command dup not valid"
        dna_to_dup = super().get_dna_data().get_sequence_by_id_or_name(command[1])
        if not dna_to_dup:
            return "id not in data"
        # get new dup seq name
        new_name = super().get_dna_data().get_next_new_name(dna_to_dup.get_dna_name())
        id = super().get_dna_data().get_next_id()
        super().get_dna_data().append_sequences(dna_to_dup.get_dna(),new_name,id,"*")
        return f"[{id}] {new_name} : {dna_to_dup.get_dna()}"
