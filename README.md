# INCode Generator
###### _in-code-generator_
Code generator for any language, java, python, node, php, etc. from Table Structure.

This is __template based__ code generator that can be adapted to generate any language code.

#### How to run

1. Take a pull ``
1. Install python.
2. Go to folder and run
`> python __init__.py --package-name com.yourcompany.yourappname`

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
  
  
1. Ex. com.yourpackage.yourappname  
`PACKAGE_NAME = '##package_name##'`
      
2. Ex. table_name (lower_snake_cased)  
`TABLE_NAME = '##table_name##'`
  
3. Ex. TableName  
`TABLE_NAME_CS = '##table_name_cs##'`
  
4. Ex. tableName  
`TABLE_NAME_LCS = '##table_name_lcs##'`
  
5. Ex. Format same as above 3  
`ID_FIELD = '##id_field##'`  
`ID_FIELD_CS = '##id_field_cs##'`  
`ID_FIELD_LCS = '##id_field_lcs##'`  
  
6. Ex. \#{fieldName}  
`ID_FIELD_LCS_HASHED = '##id_field_lcs_hashed##'`  
  
7. A random serial number.  
`GENERATED_SERIAL = '##eighteen_digit_random_number##'`  

Please refer other fields in `code_replacer.py`

#### Adopting `INCode Generator` to your needs.  
Here are some helpful instructions before you start 
adopting this code to your needs.

1. `code_replacer.py` is what you will need to modify.
2. `custom_processor` method processes every file in 
template folder.
3. Add your replacement logic to `custom_processor`
4. `custom_processor` provides  
    * `processed_contents`: TextIOWrapper (String) = already processed file contents 
    * `original_file_name`: String = Template file name, can be used to identify specific template and 
    return a partial file name which will consist in the form __\<TableName\>\<PartialFileName\>.\<ext\>__ and can be used to process template specific contents. 
    * `partial_file_name_with_ext`: String = If you are processing a table based contents, 
    __\<PartialFileName\>.\<ext\>__, will be appended at the end 
    of the table name.
    
    It also returns -
    * `processed_contents`: TextIOWrapper (String) = As the name suggests, once you are finished with processing contents, return new contents.
    * `partial_file_name_with_ext`: String = This is the same one which was available in input, although you can modify it according to your need.
    
5. Points to be considered - 
    * While suggesting PRs, please do not make code complicated, and follow the best practices of python.
    * `'deleted', 'created_at', 'created_by', 'updated_at', 'updated_by'` are the field names that will be ignored while creating tables. Reason being that they are common and being handled as deemed necessary.
    * `'constraint'` or `');'` are termination sequences.

6. Although this program primarily focuses on 
Code Generation, it can be transformed into any 
text replacement needs, such as generating a 
letter to all of your employees. :D  
    

#### Contribution
1. Raise an issue, a community discussion will decide the necessity of a feature. 
2. PRs are welcome.
3. Templates are welcome too. Just make sure that you are covering all you your needs in single go.

#### Thank you!

For all the inspirations and help from my friends and colleagues, more to some especially inspiring peoples. (Names are dropped upon their request.)

#### No Association Declaration

This library is my personal work and is no way associated to my current and previous employer(s).

#### License  
GNU General Public License v3.0  
  
  
[//]: # (_keywords: python, java, code, generator, code-generator, code generator, file generator, c, cpp, c++, free code, latest code generator, free code generator, mybatis, python code generator, sql, mysql, postgres, code for postgres_)
