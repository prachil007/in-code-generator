# Error Codes
# 1 - File does not exist
# 2 - Incorrect table structure
# 3 - Directory does not exist
# 4 - File export error
# 5 - Insufficient number of fields


class ErrorHandler:

    @classmethod
    def no_file_exit(cls, file_name: str):
        print('File does not exists: ' + file_name)
        exit(1)

    @classmethod
    def table_structure(cls):
        print('Please check appropriate table structure.')
        exit(2)

    @classmethod
    def no_dir_exit(cls, dir_name: str):
        cls.no_dir(dir_name)
        exit(3)\

    @classmethod
    def no_dir(cls, dir_name: str):
        print('Directory does not exists: ' + dir_name)

    @classmethod
    def file_export_failed_exit(cls, file_name: str, error):
        print('File export error: ' + file_name + '\nError: ' + error)
        exit(4)

    @classmethod
    def insufficient_fields_exit(cls):
        print('At least two fields must be there to create table.')
        exit(5)
