from command.manipulation_commands.manipulation_commands import Manipulation_Command


class Command_Slice(Manipulation_Command):
    """
    slice seq in given indexes
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Slice.__instance:
            Command_Slice.__instance = object.__new__(cls)
        return Command_Slice.__instance

    def execute(self, command):
        super().init_command(command)
        error = super().check_command()
        if error:return error
        try:
            3 <= len(command) <= 6
        except ValueError:
            return "invalid command slice"
        # get seq to slice
        dna_to_slice = super().execute()
        dna_data = dna_to_slice.get_dna()
        if len(dna_data) < int(command[3]):
            return "index to slice out of range"
        try:
            # slice seq
            new_dna_seq = dna_data[int(command[2]) :int(command[3])]
            dna_to_slice.set_dna(new_dna_seq)
        except IndexError:
            return "index to slice out of range"
        # change after slice
        return super().change_given_seq(new_dna_seq, dna_to_slice,"s")
