from command.command import Command


class Sequences_Analysis(Command):
    """
    shared class for sequences analysis command
    """
    __command = None
    __dna_to_change = None

    def init_command(self, command):
        self.__command = command

    def check_command(self):
        try:
            len(self.__command) == 3
        except IndexError:
            return "command not valid"

    def execute(self, *args):
        """
        return seq to analysis in and sub string
        """
        seq_to_find_in = super().get_dna_data().get_sequence_by_id_or_name(self.__command[1])
        if self.__command[2][0] in ['#', '@']:
            sub_seq = super().get_dna_data().get_sequence_by_id_or_name(self.__command[2]).get_dna()
            if not sub_seq: return "seq to find not found"
        else:
            sub_seq = self.__command[2]
        return seq_to_find_in, sub_seq
