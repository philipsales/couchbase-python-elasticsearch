HOW TO CREATE A MAPPING FORMAT USING CSV (DATA PIPELINE)

Order of headers in csv:
    Column 1. parent_key_name
    Column 2. key_to
    Column 3. key_from
    Column 4. default_value
    Column 5. fields_for_computation
    Column 6. to_compute
    Column 7. type

Parent key name (parent_key_name):
    - IF THERE IS NO PARENT: LEAVE BLANK
    - Should be flattened if mulitple
    For example: 
    {
        health_informations: {
            blood_pressure: {
                first_reading: {
                    systole: "",
                    diastole: ""
                }
            }
        }
    }

    The parent of 'systole' should be: 
        "health_informations.blood_pressure.first_reading"

    Then the leaf, which in this case is 'systole', will go to the 'key_to' field.
    Remember that 'parent_key_name' is for 'key_to' field only

Key to (key_to):
    LEAF value of the OUTPUT SCHEMA matching the 'key_from'
    IF 'KEY TO' field has a parent, put the parent the way it is written
    in the 'parent_key_name' instructions

Key from (key_from):
    IF THERE ARE NO FIELDS FROM INPUT SCHEMA: LEAVE BLANK
    leaf value of the INPUT SCHEMA matching the 'key_to'
    IF 'KEY FROM' has a parent. For this example:
    {
        health_informations: {
            blood_pressure: {
                first_reading: {
                    systole: ""
                    diastole: ""
                }
            }
        }
    }

    It should be written this way in the 'key_from' field:
        health_informations.blood_pressure.first_reading.systole

    No need for single quotes or double quotes.


Default value (default_value):
    IF THERE ARE NO DEFAULT VALUE INTENDED: LEAVE BLANK
    If date: date_now
    If string: (enter any string if any. if there are no strings, it will be assumed as blank)
    If array: (LEAVE BLANK when no initial value; enter default string if any; date_now if date)
    if boolean: (LEAVE BLANK if default value is FALSE; IF TRUE, write true)
    if integer: (LEAVE BLANK if default value is 0; IF ANY NUMBER, write the number)
    if float: (LEAVE BLANK if default value is 0.0; IF ANY FLOAT NUMBER, write the float number)

To compute (to_compute):
    IF THERE ARE NO COMPUTATION: LEAVE BLANK
    If there are any computation: write 'true'

Fields for computation (fields_for_computation):
    - IF THERE ARE NO COMPUTATION: LEAVE BLANK
    - If there are any computation, make sure to write the key fields in flatten way
    For example you are looking for the 'height' and 'weight' for 'bmi',
    Here is how it looks like in the json:
    {
        health_informations: {
            weight: 50,
            height: 161,
            ...
        }
    }

    The given will be entered as follows in the cell: 
        health_informations.height,health_informations.weight

    - Note that there is no need for double quotes or single quotes.
    - If more than 1 field is needed for computation, separate them with comma (,)

Type (type):
    Different data types THAT CAN BE READ by the data pipeline:
    - integer
    - float
    - string
    - array
    - boolean
    - date