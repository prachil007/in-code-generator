from io import TextIOWrapper

from error_handler import ErrorHandler
from models.file_content import FileContent


class CodeProcessor:

    @classmethod
    def process_file_contents(cls, contents: TextIOWrapper) -> FileContent:

        table_name: str = ''
        field_list: [{str, str}] = []
        table_started: bool = False
        table_ended: bool = False

        for new_line in contents:
            line = new_line.lower()
            if 'create table' in line:
                split_array = line.replace('create table', '').strip().split(' ')
                table_started = True
                if len(split_array) > 1:
                    table_name = split_array[0]
                    print('Table name : ' + table_name)
                continue

            split_array = []
            if table_started:
                split_array = line.strip().split(' ')

            for text in split_array:
                if ('deleted' == text) | ('created_at' in text) | ('created_by' in text) | \
                        ('updated_at' == text) | ('updated_by' == text) | \
                        (');' == text) | ('constraint' in line):
                    table_started = False
                    table_ended = True

            if table_started:
                line_str_array: [str] = line.strip().split(' ')
                if len(line_str_array) >= 1:
                    field = {
                        'name': line_str_array[0],
                        'data_type': line_str_array[1]
                    }
                    field_list.append(field)

            if table_ended:
                break

        if table_started:
            ErrorHandler.table_structure()

        file_contents = FileContent(table_name, field_list)
        if len(file_contents.field_list) <= 2:
            ErrorHandler.insufficient_fields_exit()
        return file_contents

    @classmethod
    def print(cls, file_contents: FileContent):
        print('\nFinal table name: ' + file_contents.table_name)
        print('\nFinal table name CCL: ' + file_contents.table_name_lcs)
        print('\nFinal table name CCC: ' + file_contents.table_name_cs)
        for field in file_contents.field_list:
            print('\n Field: ' + field.name + ', ' + field.name_cs)
