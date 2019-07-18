# in-code-generator
Code generator for any language, java, python, node, php, etc. from Table Structure.

This is __template based__ code generator that can be adapted to generate any language code.

#### Program Arguments
`--input` - this argument can be use to specify input file name.   
_Default: ./input.sql_ 
  
`--package-name` - this argument can be use to specify input file name.   
_Default: com.yourcompany.yourappname_
   
#### Output
New `./output` directory will be generated upon every execution.
For each table, a new sub folder will be generated.

#### Available variables to use in template and code replacements. 
Refer `code_replacer.py`  for more replacement variables.  
To write your own replacement logic, use  
`def custom_processor(processed_contents, original_file_name: str, partial_file_name_with_ext: str)`  
  
  
Ex. com.yourpackage.yourappname  
`PACKAGE_NAME = '##package_name##'`
      
Ex. table_name (lower_snake_cased)  
`TABLE_NAME = '##table_name##'`
  
Ex. TableName  
`TABLE_NAME_CS = '##table_name_cs##'`
  
Ex. tableName  
`TABLE_NAME_LCS = '##table_name_lcs##'`
  
Ex. Format same as above 3  
`ID_FIELD = '##id_field##'`  
`ID_FIELD_CS = '##id_field_cs##'`  
`ID_FIELD_LCS = '##id_field_lcs##'`  
  
Ex. \#{fieldName}  
`ID_FIELD_LCS_HASHED = '##id_field_lcs_hashed##'`  
  
Need in model class.  
`GENERATED_SERIAL = '##eighteen_digit_random_number##'`  
  
  
#### License  
GNU General Public License v3.0  
  
