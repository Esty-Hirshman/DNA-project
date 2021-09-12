from dna.dna_sequence import Dna_Sequence


class DNA_Data:
    __instance = None
    __dna_name_dict = {}
    __dna_id_dict = {}

    def __new__(cls, *args, **kwargs):
        if not DNA_Data.__instance:
            DNA_Data.__instance = object.__new__(cls)
        return DNA_Data.__instance

    def get_sequence_by_id_or_name(self, seq):
        """
        get seq by name if given seq is name or by id if given seq is id
        :param seq: seq name or id
        :return: sequence if exist else return False
        """
        if seq[0] == "#":
            seq = seq.replace("#", "")
            if int(seq) in self.__dna_id_dict:
                name_to_return = self.__dna_id_dict[int(seq)]["name"]
                return self.__dna_name_dict[name_to_return]
            else:
                return False
        else:
            seq = seq.replace("@", "")
            if seq in self.__dna_name_dict:
                return self.__dna_name_dict[seq]
            else:
                return False

    def is_name_taken(self, name):
        """
        check if given name is already used in data base
        :param name: name to check is exist
        :return: True if name exist else False
        """
        if name in self.__dna_name_dict:
            return True
        return False

    def get_next_id(self):
        """
        get the next id in dna data base by length of data
        :return: next id
        """
        return len(self.__dna_id_dict) + 1

    def append_sequences(self, sequence, name, id, status):
        """
        add sequence to data
        :param sequence: dna string
        :param name: dna name
        :param id: dna id
        """
        try:
            self.__dna_name_dict[name] = Dna_Sequence(sequence, name, id)
            self.__dna_id_dict[id] = {"name": name, "status": status}
        except ValueError:
            raise ValueError

    def get_next_new_name(self, name, string_in_name=""):
        """
        returns the next name if the seq name is not sent in the manipulation command
        :param name: old name of seq
        :param string_in_name: string to add to new name
        :return:new name
        """
        index_name = 1
        new_name = f"{name}_{string_in_name}{index_name}"
        while self.is_name_taken(new_name):
            index_name += 1
            new_name = f"{name}_{string_in_name}{index_name}"
        return new_name

    def delete_sequence(self, sequence):
        """
        delete given sequence from data
        :param sequence: to delete
        """
        try:
            del self.__dna_name_dict[sequence.get_dna_name()]
            del self.__dna_id_dict[sequence.get_dna_id()]
        except ValueError:
            raise ValueError

    def set_status(self, id, status):
        """
        set seq status
        :param id: seq id
        :param status: new status
        """
        name = self.__dna_id_dict[id]["name"]
        self.__dna_id_dict[id] = {"name": name, "status": status}

    def get_all_sequences(self):
        """
        get all sequences in string
        """
        res = []
        for id in self.__dna_id_dict.keys():
            dna_seq = self.__dna_name_dict[self.__dna_id_dict[id]["name"]].get_dna()
            if len(dna_seq) > 40:
                dna_seq = dna_seq[0:32:] + "..." + dna_seq[-3::]
            res.append(f"{self.__dna_id_dict[id]['status']} [{id}] {self.__dna_id_dict[id]['name']} : {dna_seq}")
        return res

    def get_num_new_seq(self):
        """
        get number of new sequences
        """
        counter = 0
        for id in self.__dna_id_dict.keys():
            if self.__dna_id_dict[id]["status"] == "o":
                counter += 1
        return counter

    def get_num_modified_seq(self):
        """
        get number of modified sequences that were not saved
        """
        counter = 0
        for id in self.__dna_id_dict.keys():
            if self.__dna_id_dict[id]["status"] == "*":
                counter += 1
        return counter
