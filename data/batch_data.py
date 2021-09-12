class Batch_Data:
    __instance = None
    __batches = {}

    def __new__(cls, *args, **kwargs):
        if not Batch_Data.__instance:
            Batch_Data.__instance = object.__new__(cls)
        return Batch_Data.__instance

    def is_name_in(self, name):
        """
        check if name of batch is already in
        """
        return name in self.__batches

    def append_batch(self, name, batch_commands):
        """
        add batch to data
        :param name: batch name
        :param batch_commands: batch commands
        """
        self.__batches[name] = batch_commands

    def get_batch_by_name(self, name):
        """
        get commands batch by batch name
        :param name: batch name to get
        """
        try:
            return self.__batches[name]
        except KeyError:
            raise KeyError

    def get_all_batches(self):
        """
        get all batches names in array
        """
        return self.__batches.keys()
