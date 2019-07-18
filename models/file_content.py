from utils.number_utils import NumberUtils
from utils.str_utils import StrUtils
from models.field import Field


class FileContent:
    package_name: str = ''
    table_name: str = ''
    table_name_cs: str = ''
    table_name_lcs: str = ''
    field_list: [Field] = []
    generated_serial: int = 0

    def __init__(self, table_name: str, field_list: [{str, str}]) -> object:
        self.generated_serial = NumberUtils.random(18)
        self.table_name = table_name
        self.table_name_lcs = StrUtils.camel_cased_name(table_name)
        self.table_name_cs = StrUtils.capitalise_first_letter_camel_cased_name(table_name)

        self.field_list = list(map(lambda field: Field(field['name'], field['data_type']), field_list))





