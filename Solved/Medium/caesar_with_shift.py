import string
def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        lower_keys = list(lower)
        lower_values = list(lower)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
        upper_keys = list(upper)                 
        upper_values = list(upper)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        shift_dict = dict(zip(full_keys, full_values))
        return shift_dict        

for t in range(int(input())):
    strings = input()
    shift_vals = input().split()
    left_right = input().split()
    if len(strings)//len(left_right) > 0:
        left_right = left_right * len(strings)
    if len(strings)//len(shift_vals) > 0:
        shift_vals = shift_vals * len(strings)
    shift = 0
    ans  = ""
    for i in strings:
        if i.isalpha():
            if int(left_right[shift]) == 1:
                shift_dict = build_shift_dict(-1*int(shift_vals[shift]))
                ans += shift_dict[i]
                shift+=1
            else:
                shift_dict = build_shift_dict(int(shift_vals[shift]))
                ans += shift_dict[i]
                shift+=1
                
        else:
            ans+=i
    print(ans.lower())