from command.manipulation_commands.manipulation_commands import Manipulation_Command


class Command_Replace(Manipulation_Command):
    """
    replace nucleotide in seq in given indexes to given new nucleotides
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Replace.__instance:
            Command_Replace.__instance = object.__new__(cls)
        return Command_Replace.__instance

    def execute(self, command):
        super().init_command(command)
        error = super().check_command()
        if error: return error
        if len(command) < 4:
            return "command replace nod valid, missing args"
        # seq to replace in
        dna_to_change = super().execute()
        if not dna_to_change:
            return "seq not found"
        # replace all given indexes
        index, finish_index = 2, len(command) - 3 if ":" in command else len(command) - 1
        while index < finish_index:
            try:
                dna_to_change[int(command[index])] = command[index + 1]
            except ValueError:
                return f"invalid value {command[index + 1]}"
            index += 2
        # change to replaced seq
        return super().change_given_seq(dna_to_change.get_dna(), dna_to_change, "r")
