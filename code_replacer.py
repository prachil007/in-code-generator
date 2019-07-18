import re
from enum import Enum

from models.file_content import FileContent


class ReplacementStrings(Enum):
    # Ex. com.yourpackage.yourappname
    PACKAGE_NAME = '##package_name##'
    # Ex. table_name (lower_snake_cased)
    TABLE_NAME = '##table_name##'
    # Ex. TableName
    TABLE_NAME_CS = '##table_name_cs##'
    # Ex. tableName
    TABLE_NAME_LCS = '##table_name_lcs##'
    # Ex. Same as above 3
    FIELD = '##field##'
    FIELD_CS = '##field_cs##'
    FIELD_LCS = '##field_lcs##'
    # Ex. #{fieldName}
    FIELD_LCS_HASHED = '##field_lcs_hashed##'
    # Comma separated list of above fields
    FIELD_LIST = '##field_list##'
    FIELD_LIST_CS = '##field_list_cs##'
    FIELD_LIST_LCS = '##field_list_lcs##'
    FIELD_LIST_LCS_HASHED = '##field_list_lcs_hashed##'
    FIELD_LIST_LCS_MODEL_HASHED = '##field_list_lcs_modelhashed##'
    # Possible Data types - String, Long, Double, boolean
    FIELD_DATA_TYPE = '##field_data_type##'
    # Need in model class.
    GENERATED_SERIAL = '##eighteen_digit_random_number##'

    MODEL_ROW = 'private ##field_data_type## ##field_lcs##;'
    ID_EQUAL_XML_ROW = '##id_field## = ##id_field_hashed##'
    NO_ID_FIELD_LIST_HASHED_XML_ROW = '##field_list_no_id## = ##field_list_no_id_lcs_hashed##'
    ID_FIELD = '##id_field##'
    ID_FIELD_CS = '##id_field_cs##'
    ID_FIELD_LCS = '##id_field_lcs##'
    ID_FIELD_LCS_HASHED = '##id_field_lcs_hashed##'


class CodeReplacer:
    file_contents: FileContent

    def __init__(self, file_contents):
        self.file_contents = file_contents

    def __dao_impl_processor__(self, processed_contents):

        regex1 = re.compile(r'(.*)' + ReplacementStrings.FIELD_LCS.value +
                            '(.*)' + ReplacementStrings.FIELD.value +
                            '(.*)', re.IGNORECASE)
        regex2 = re.compile(r'(.*)' + ReplacementStrings.NO_ID_FIELD_LIST_HASHED_XML_ROW.value +
                            '(.*)', re.IGNORECASE)
        results_list_content = ''
        no_id_field_list_content = ''
        for field in self.file_contents.field_list:
            results_row = '\t\t<result property="' + field.name_lcs + '" column="' + field.name + '" />'
            results_list_content = results_list_content + '\n' + results_row
            if field != self.file_contents.field_list[0]:
                no_id_field_row = '\t\t\t' + field.name + ' = ' + field.name_lcs_hashed + ','
                if no_id_field_list_content != '':
                    no_id_field_list_content = no_id_field_list_content + '\n' + no_id_field_row
                else:
                    no_id_field_list_content = no_id_field_row
        processed_contents = re.sub(regex1, r'' + results_list_content, processed_contents)
        processed_contents = re.sub(regex2, r'' + no_id_field_list_content, processed_contents)

        mapped_field_list = map(lambda f: f.name, self.file_contents.field_list)
        joined_field_list = ", ".join(mapped_field_list)
        processed_contents = processed_contents.replace(ReplacementStrings.FIELD_LIST.value, joined_field_list)

        mapped_field_list_lcs = map(lambda f: f.name_lcs_hashed, self.file_contents.field_list)
        joined_field_list_lcs = ", ".join(mapped_field_list_lcs)
        processed_contents = processed_contents.replace(ReplacementStrings.FIELD_LIST_LCS_HASHED.value,
                                                        joined_field_list_lcs)

        mapped_field_list_lcs_model = map(lambda f: "#{model." + f.name_lcs + "}", self.file_contents.field_list)
        joined_field_list_lcs_model = ", ".join(mapped_field_list_lcs_model)
        processed_contents = processed_contents.replace(ReplacementStrings.FIELD_LIST_LCS_MODEL_HASHED.value,
                                                        joined_field_list_lcs_model)

        return processed_contents

    def __model_processor__(self, processed_contents):

        regex = re.compile(r'(.*)' + ReplacementStrings.FIELD_DATA_TYPE.value +
                           '.*' + ReplacementStrings.FIELD_LCS.value + ';', re.IGNORECASE)

        field_list_content = ''
        for field in self.file_contents.field_list:
            replacement_row = '\tprivate ' + field.data_type + ' ' + field.name_lcs + ';'
            field_list_content = field_list_content + '\n' + replacement_row

        processed_contents = re.sub(regex, r'' + field_list_content, processed_contents)

        return processed_contents

    def common_processor(self, template_contents):
        processed_contents = template_contents.read()
        processed_contents = processed_contents.replace(ReplacementStrings.PACKAGE_NAME.value,
                                                        self.file_contents.package_name)
        processed_contents = processed_contents.replace(ReplacementStrings.TABLE_NAME.value,
                                                        self.file_contents.table_name)
        processed_contents = processed_contents.replace(ReplacementStrings.TABLE_NAME_CS.value,
                                                        self.file_contents.table_name_cs)
        processed_contents = processed_contents.replace(ReplacementStrings.TABLE_NAME_LCS.value,
                                                        self.file_contents.table_name_lcs)
        processed_contents = processed_contents.replace(ReplacementStrings.GENERATED_SERIAL.value,
                                                        str(self.file_contents.generated_serial))
        processed_contents = processed_contents.replace(ReplacementStrings.ID_FIELD.value,
                                                        self.file_contents.field_list[0].name)
        processed_contents = processed_contents.replace(ReplacementStrings.ID_FIELD_CS.value,
                                                        self.file_contents.field_list[0].name_cs)
        processed_contents = processed_contents.replace(ReplacementStrings.ID_FIELD_LCS.value,
                                                        self.file_contents.field_list[0].name_lcs)
        processed_contents = processed_contents.replace(ReplacementStrings.ID_FIELD_LCS_HASHED.value,
                                                        self.file_contents.field_list[0].name_lcs_hashed)
        return processed_contents

    @staticmethod
    def custom_processor(processed_contents, original_file_name: str, partial_file_name_with_ext: str):
        print('Original file name: ' + original_file_name + '\t\tPartial file name: ' + partial_file_name_with_ext)
        return processed_contents, partial_file_name_with_ext
