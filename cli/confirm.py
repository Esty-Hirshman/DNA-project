from cli.cli import CLI


class Confirm(CLI):
    """
    confirm class inherit CLI to handle when need to confirm something
    """
    def __init__(self):
        super().__init__(None)

    def run(self, massage):
        super().set_prompt(f"{massage} Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.\n> confirm >>>")
        while True:
            command = input(super().get_prompt())
            command = command.strip().split()
            if command[0] not in ['Y', 'y', 'N', 'n']:
                super().set_prompt(
                    "You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.\n> confirm >>>")
            else:
                if command[0] in ["Y", "y"]:
                    return True
                else:
                    super().set_prompt(
                        f"{massage} Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.\n> confirm >>>")
                    return False
