import re


class printf:
    def __init__(self, in_format_string: str, in_args: list) -> None:
        self.format_string: str = in_format_string
        self.args: list = in_args
        self.width: int = 0

    def convert(self):
        # Split the format string into a list of strings and format specifiers (e.g. "%s") but not \%[A-Za-z] but keep the string
        # so if \%s is found, it is not split
        format_ = re.split(r'((?<!\\)%[A-Za-z])', self.format_string)
        # loop through list and check for valid format specifiers
        counter = -1
        for i in range(len(format_)):
            # if the string is a format specifier
            if format_[i].startswith('%'):
                counter += 1
                # remove the first character
                format_[i] = format_[i][1:]
                # if the first character is a number, it is the index of the argument to use
                # if the first character is a special character, it is a special format specifier
                # | Format Specifier | Output                                                       |
                # |------------------|--------------------------------------------------------------|
                # | `%10d`           | integer with a minimum width of 10 characters, right-aligned |
                # | `%-10s`          | string with a minimum width of 10 characters, left-aligned   |
                # | `%.2f`           | floating-point number with 2 decimal places of precision     |
                # | `%#x`            | hexadecimal integer with the `0x` prefix                     |
                # | `%+d`            | signed integer with a plus sign (+) for positive numbers     |
                # all valid specifiers
                left_align = False
                precision_valid = False
                precision = ""
                if format_[i][0] == '-':
                    left_align = True
                    format_[i] = format_[i][1:]
                elif format_[i][0] == '.':
                    # remove the dot
                    format_[i] = format_[i][1:]
                    # the next characters are the precision till the next character that is not a digit
                    for j in range(len(format_[i])):
                        if not format_[i][j].isdigit():
                            break
                        precision += format_[i][j]
                    # remove the precision from the format string
                    format_[i] = format_[i][len(precision):]
                    # convert the precision to an integer
                    precision = int(precision)
                    precision_valid = True
                if format_[i][0].isdigit():
                    # take the full integer as teh size
                    size_str = ""
                    for j in range(len(format_[i])):
                        if not format_[i][j].isdigit():
                            break
                        size_str += format_[i][j]
                    # remove the size from the format string
                    format_[i] = format_[i][len(size_str):]
                    # convert the size to an integer
                    self.width = int(size_str)
                # replace the format specifier with the argument
                # check first if the format specifier is in the list of valid specifiers
                if format_[i][0] in ['d', 'i', 'u', 'o', 'x', 'X', 'f', 'F', 'e', 'E', 'g', 'G', 'a', 'A', 'c', 's', 'p',
                                        'n']:
                        # if the format specifier is a string
                        arg = self.args[counter]
                        # if the format specifier is an integer
                        if format_[i][0] in ['d', 'i', 'u', 'o', 'x', 'X']:
                            # if the precision is valid
                            if precision_valid:
                                format_[i] = arg
                                continue
                            # if the integer is shorter than the size
                            if len(str(arg)) < self.width:
                                # if the integer is left-aligned
                                if left_align:
                                    # add spaces to the right of the integer
                                    arg = str(arg) + " " * (self.width - len(str(arg)))
                                # if the integer is right-aligned
                                else:
                                    # add spaces to the left of the integer
                                    arg = " " * (self.width - len(str(arg))) + str(arg)
                            format_[i] = arg
                        # if the format specifier is a floating-point number
                        elif format_[i][0] in ['f', 'F', 'e', 'E', 'g', 'G', 'a', 'A']:
                            # if the precision is valid
                            if precision_valid:
                                # if the number after the dot is longer than the precision
                                if len(str(arg).split('.')[1]) > precision:
                                    # truncate the number
                                    arg = str(arg)[:precision]
                                format_[i] = arg
                                continue
                            # if the number is shorter than the size
                            if len(str(arg)) < self.width:
                                # if the number is left-aligned
                                if left_align:
                                    # add spaces to the right of the number
                                    arg = str(arg) + " " * (self.width - len(str(arg)))
                                # if the number is right-aligned
                                else:
                                    # add spaces to the left of the number
                                    arg = " " * (self.width - len(str(arg))) + str(arg)
                            format_[i] = arg
                        # if the format specifier is a character
                        elif format_[i][0] == 'c':
                            # if the precision is valid but is not float than continue
                            if precision_valid:
                                format_[i] = arg
                                continue
                            # if the character is shorter than the size
                            if len(str(arg)) < self.width:
                                # if the character is left-aligned
                                if left_align:
                                    # add spaces to the right of the character
                                    arg = str(arg) + " " * (self.width - len(str(arg)))
                                # if the character is right-aligned
                                else:
                                    # add spaces to the left of the character
                                    arg = " " * (self.width - len(str(arg))) + str(arg)
                            format_[i] = arg
                        # if the format specifier is a string
                        elif format_[i][0] == 's':
                            # if the precision is valid
                            if precision_valid:
                                format_[i] = arg
                                continue
                            # if the string is shorter than the size
                            if len(str(arg)) < self.width:
                                # if the string is left-aligned
                                if left_align:
                                    # add spaces to the right of the string
                                    arg = str(arg) + " " * (self.width - len(str(arg)))
                                # if the string is right-aligned
                                else:
                                    # add spaces to the left of the string
                                    arg = " " * (self.width - len(str(arg))) + str(arg)
                            format_[i] = arg
        return "".join(format_)






if __name__ == '__main__':
    print_ = printf("Hello, %s", ["World"])
    ob = print_.convert()
    print(ob)