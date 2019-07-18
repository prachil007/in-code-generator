import sys

from code_processor import CodeProcessor
from file_processor import FileProcessor
from models.file_content import FileContent

DEFAULT_PACKAGE_NAME = 'com.yourcompany.yourappname'
DEFAULT_INPUT_FILE_NAME = './input.sql'


def parse_args():
    package_name = ''
    input_file_path = ''
    found_package_name = False
    found_file_path = False
    for arg in sys.argv:
        if found_package_name:
            package_name = arg
            found_package_name = False
        if arg == '--package-name':
            found_package_name = True
        if found_file_path:
            input_file_path = arg
            found_file_path = False
        if arg == '--input':
            found_file_path = True
    if package_name != '':
        print('Using package name: {}'.format(package_name))
    else:
        package_name = DEFAULT_PACKAGE_NAME
        print('Using default package name: {}'.format(DEFAULT_PACKAGE_NAME))
    if input_file_path != '':
        print('Using input file: {}'.format(input_file_path))
    else:
        input_file_path = DEFAULT_INPUT_FILE_NAME
        print('Using default input file: {}'.format(DEFAULT_INPUT_FILE_NAME))
    return input_file_path, package_name


def main():
    print('IN Code Generator started....\nAnalysing input file...')

    input_file_path, package_name = parse_args()

    input_file_contents = FileProcessor.get_file_contents(input_file_path)
    if input_file_contents:
        file_content: FileContent = CodeProcessor.process_file_contents(input_file_contents)
        file_content.package_name = package_name
        if file_content:
            file_exports: FileProcessor = FileProcessor(file_content)
            file_exports.process_and_export_templates()


if __name__ == '__main__':
    main()
