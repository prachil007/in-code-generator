from typing import List


class StrUtils:

    @staticmethod
    def camel_cased_name(table_name) -> str:
        all_indexes: List[int] = ([pos for pos, char in enumerate(table_name) if char == '_'])
        lower_cased_name = table_name.lower()
        for idx in all_indexes:
            if idx + 2 < len(lower_cased_name):
                lower_cased_name = lower_cased_name[:idx + 1] + lower_cased_name[idx + 1].upper() +\
                                             lower_cased_name[idx + 2:]
            elif idx + 1 < len(lower_cased_name):
                lower_cased_name = lower_cased_name[:idx + 1] + lower_cased_name[idx + 1].upper()
        return lower_cased_name.replace('_', '')

    @staticmethod
    def capitalise_first_letter_camel_cased_name(string):
        temp_string = StrUtils.camel_cased_name(string)
        length = len(temp_string)
        if length > 1:
            temp_string = temp_string[:0] +  temp_string[0].upper() + temp_string[1:]
        return temp_string
