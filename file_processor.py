import os
import shutil

from code_replacer import CodeReplacer
from error_handler import ErrorHandler
from models.file_content import FileContent
from utils.obj_utils import ObjectUtils


# Replacement abbreviation
# CS - CamelCased, LCS - CamelCased with 1st character lowercase

class FileProcessor:
    OUTPUT_DIR = './output/'
    TEMPLATE_DIR = './templates/'

    file_contents: FileContent = None

    def __init__(self, file_contents: FileContent):
        self.file_contents = file_contents

    @classmethod
    def get_file_contents(cls, file_name: str):
        try:
            input_file = open(file_name, 'r')
            if input_file.mode == 'r':
                return input_file
            pass
        except FileNotFoundError:
            ErrorHandler.no_file_exit(file_name)
            pass
        finally:
            pass
        return None

    def process_and_export_templates(self):
        if not ObjectUtils.exists(self.file_contents):
            return

        self.__check_output_path__(self.file_contents.table_name)

        for (root, dirs, files) in os.walk(self.TEMPLATE_DIR, topdown=True):
            for file_name in files:
                self.__process_file__(self.TEMPLATE_DIR + '/' + file_name)

    @classmethod
    def __check_output_path__(cls, subdir_name):

        output_dir_path = FileProcessor.OUTPUT_DIR
        shutil.rmtree(output_dir_path)
        if subdir_name:
            output_dir_path = FileProcessor.OUTPUT_DIR + subdir_name
        os.makedirs(output_dir_path, exist_ok=True)
        print('Output dir: ' + output_dir_path)

    def __process_file__(self, original_file_name: str):
        template_contents = self.get_file_contents(original_file_name)
        code_replacer = CodeReplacer(self.file_contents)
        pre_processed_contents = code_replacer.common_processor(template_contents)

        file_name = original_file_name.lower()
        file_extension = '.' + file_name.split('.')[-1]
        post_processed_contents = pre_processed_contents
        partial_file_name = 'Generic'
        if 'daoimpl' in file_name:
            partial_file_name = ''
            post_processed_contents = code_replacer.__dao_impl_processor__(pre_processed_contents)
        elif 'model' in file_name:
            partial_file_name = ''
            post_processed_contents = code_replacer.__model_processor__(pre_processed_contents)
        elif 'dao' in file_name:
            partial_file_name = 'Dao'
        elif 'service' in file_name:
            partial_file_name = 'Service'

        partial_file_name_with_ext = partial_file_name + file_extension
        post_processed_contents, partial_file_name_with_ext = code_replacer.custom_processor(post_processed_contents,
                                                                                             original_file_name,
                                                                                             partial_file_name_with_ext)
        self.__export_file__(post_processed_contents, partial_file_name_with_ext)

    def __export_file__(self, file_contents: str, suffix: str):
        error = None
        export_file_name = self.__get_export_file_name__(suffix)
        try:
            f = open(export_file_name, 'w+')
            f.write(file_contents)
            f.close()
        finally:
            if error:
                ErrorHandler.file_export_failed_exit(export_file_name, None)
            else:
                print('File exported: ' + export_file_name)
            pass

    def __get_export_file_name__(self, suffix):
        return self.OUTPUT_DIR + self.file_contents.table_name + '/' + \
               self.file_contents.table_name_cs + suffix
