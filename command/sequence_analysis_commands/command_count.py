from command.sequence_analysis_commands.sequences_analysis import Sequences_Analysis


class Command_Count(Sequences_Analysis):
    """
    count number of times sub string is in seq
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Count.__instance:
            Command_Count.__instance = object.__new__(cls)
        return Command_Count.__instance

    def execute(self, command, **kwargs):
        super().init_command(command)
        error = super().check_command()
        if error: return error
        count_and_count_in = super().execute(command)
        try:
            return len(count_and_count_in[0].find_all_sub(count_and_count_in[1]))
        except ValueError:
            return f"can not find {count_and_count_in[1]} in {count_and_count_in[0].get_dna()}"
