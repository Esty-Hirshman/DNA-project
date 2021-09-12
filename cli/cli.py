class CLI:
    def __init__(self, prompt):
        self.__prompt = prompt

    def get_prompt(self):
        return self.__prompt

    def set_prompt(self, new_prompt):
        self.__prompt = new_prompt

    def run(self, *args):
        raise
