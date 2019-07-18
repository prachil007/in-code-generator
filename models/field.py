from utils.str_utils import StrUtils


class Field:
    # field_name
    name: str = ''
    # FieldName
    name_cs: str = ''
    # fieldName
    name_lcs: str = ''
    # #{fieldName}
    name_lcs_hashed: str = ''
    # Possible Types - String, Long, Double, boolean
    data_type: str = ''

    def __init__(self, field_name: str, data_type: str):
        self.name = field_name.strip('`').strip("'")
        self.name_cs = StrUtils.capitalise_first_letter_camel_cased_name(self.name)
        self.name_lcs = StrUtils.camel_cased_name(self.name)
        self.name_lcs_hashed = '#{' + self.name_lcs + '}'

        lower_cased = data_type.lower()
        if ('char' in lower_cased) | ('text' in lower_cased):
            self.data_type = 'String'
        elif ('double' in lower_cased) | ('real' in lower_cased) | ('float' in lower_cased):
            self.data_type = 'Double'
        elif 'boolean' in lower_cased:
            self.data_type = 'boolean'
        else:
            self.data_type = 'Long'
