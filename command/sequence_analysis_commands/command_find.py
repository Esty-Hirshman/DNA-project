from command.sequence_analysis_commands.sequences_analysis import Sequences_Analysis


class Command_Find(Sequences_Analysis):
    """
    find index of sub string in seq
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Find.__instance:
            Command_Find.__instance = object.__new__(cls)
        return Command_Find.__instance

    def execute(self, command, **kwargs):
        super().init_command(command)
        error = super().check_command()
        if error: return error
        find_and_find_in = super().execute(command)
        try:
            return find_and_find_in[0].find_sub_string_index(find_and_find_in[1])
        except ValueError:
            return f"can not find {find_and_find_in[1]} in {find_and_find_in[0].get_dna()}"
