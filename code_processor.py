from io import TextIOWrapper

from error_handler import ErrorHandler
from models.file_content import FileContent


REMOVABLE_FIELDS = ['deleted', 'created_at', 'created_by', 'updated_at', 'updated_by']


class CodeProcessor:

    @classmethod
    def process_file_contents(cls, contents: TextIOWrapper) -> [FileContent]:

        all_file_contents: [FileContent] = []

        table_name_plural: str = ''
        field_list: [{str, str}] = []
        table_started: bool = False
        table_ended: bool = False

        for new_line in contents:
            line = new_line.lower()
            if 'create table' in line:
                split_array = line.replace('create table', '').strip().split(' ')
                table_started = True
                if len(split_array) > 1:
                    table_name_plural = split_array[0]
                    print('Table name : ' + table_name_plural)
                continue

            split_array = []
            if table_started:
                split_array = line.strip().split(' ')

            for text in split_array:
                if 'constraint' in line or ');' in line:
                    table_started = False
                    table_ended = True

            cls.add_field(field_list, line, table_started)

            if table_ended:
                if len(field_list) > 2:
                    table_name = field_list[0]["name"][:-3]
                    new_file_contents = FileContent(table_name, table_name_plural, field_list)
                    table_name_plural = ''
                    field_list = []
                    table_started = False
                    table_ended = False
                    all_file_contents.append(new_file_contents)
                else:
                    ErrorHandler.insufficient_table_fields(table_name_plural)

        if table_started:
            ErrorHandler.table_structure()

        return all_file_contents

    @classmethod
    def add_field(cls, field_list, line, table_started):
        if table_started:
            line_str_array: [str] = line.strip().split(' ')
            if len(line_str_array) > 1:
                if line_str_array[0] not in REMOVABLE_FIELDS:
                    field = {
                        'name': line_str_array[0],
                        'data_type': line_str_array[1]
                    }
                    field_list.append(field)

    @classmethod
    def print(cls, file_contents: FileContent):
        print('\nFinal table name: ' + file_contents.table_name)
        print('\nFinal table name CCL: ' + file_contents.table_name_lcs)
        print('\nFinal table name CCC: ' + file_contents.table_name_cs)
        for field in file_contents.field_list:
            print('\n Field: ' + field.name + ', ' + field.name_cs)
