from command.sequence_analysis_commands.sequences_analysis import Sequences_Analysis


class Command_Findall(Sequences_Analysis):
    """
    find all indexes of  sub-string motifs in seq
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Findall.__instance:
            Command_Findall.__instance = object.__new__(cls)
        return Command_Findall.__instance

    def execute(self, command, **kwargs):
        super().init_command(command)
        error = super().check_command()
        if error: return error
        find_all_and_find_in = super().execute(command)
        try:
            res = find_all_and_find_in[0].find_all_sub(find_all_and_find_in[1])
            # return res as string
            res_string = ""
            for i in res:
                res_string += (str(i) + " ")
            return res_string
        except ValueError:
            return f"can not find {find_all_and_find_in[1]} in {find_all_and_find_in[1].get_dna()}"
