#Custom String Formatter
def format_str(s,operations):
    def _uppercase(string):
        str_list=list(string) #ha7wel el string le list of characters so i can modify it
        for x in range(len(string)):
            str_list[x]=ord(str_list[x])   #convert to ascii
            str_list[x]-=32  #uppercase conversion
            str_list[x]=chr(str_list[x])  #from ascii to charcaters
        upper_str = ''.join(str_list)
        return upper_str
        #end of uppercase function
        
    def _reverse(string):
        str_list=list(string)
        y=len(string)-1
        for x in range(len(string)//2):
            temp=str_list[x]
            str_list[x]=str_list[y]
            str_list[y]=temp
            y-=1
        rev_str = ''.join(str_list)
        return rev_str
        #end of reverse function
    
    
    def _capitalize(string):
        ascii_value=ord(string[0])
        ascii_value-=32
        char = chr(ascii_value)
        cap_str=string.replace(string[0],char)
        return cap_str
    #end of capitalize function
    
    def _apply_operation(string, operation):
        if callable(operation):   #checks if operation is a callable function
            return operation(string)
        elif operation == 'uppercase':
            return _uppercase(string)
        elif operation == 'reverse':
            return _reverse(string)
        elif operation == 'capitalize':
            return _capitalize(string)
        else:
            raise ValueError(f"Unsupported operation: {operation}")
    
    for operation in operations:
        s = _apply_operation(s, operation)
    return s


s = "hello world"
operations = ['uppercase', 'reverse']
print(format_str(s, operations))  
s = "hello world"
operations = ['capitalize', lambda x: x +' '+ 'Guest']
print(format_str(s, operations))  

