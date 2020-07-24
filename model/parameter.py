import rstr
import string
import numpy


class Parameter:
    def __init__(self, name, type, required):
        self.name = name
        self.type = type
        self.required = required

    def print_parameter(self):
        print(f'name = {self.name}, type = {self.type}, required = {self.required}')

    def empty_string(self):
        return ""

    def space(self):
        return " "

    def none(self):
        return None

    def digits_string(self):
        return "123"

    def latin_string(self):
        return "lat"

    def cyrillic_string(self):
        return "ы"

    def special_chars_string(self):
        return "?!"


class Number(Parameter):
    def __init__(self, name, required, minvalue=None, maxvalue=None, type='int32'):
        Parameter.__init__(self, name, type, required)
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def min_value(self):
        if self.minvalue is None:
            if self.type == 'int32':
                return -2147483648
            else:  # 'int64'
                return -9223372036854775808
        else:
            return self.minvalue

    def max_value(self):
        if self.maxvalue is None:
            if self.type == 'int32':
                return 2147483647
            else:  # 'int64'
                return 9223372036854775807
        else:
            return self.maxvalue

    def greater_than_max_value(self):
        if self.maxvalue is None:
            if self.type == 'int32':
                return 2147483648
            else:  # 'int64'
                return 9223372036854775808
        else:
            return self.maxvalue + 1

    def less_than_min_value(self):
        if self.minvalue is None:
            if self.type == 'int32':
                return -2147483649
            else:  # 'int64'
                return -9223372036854775809
        else:
            return self.minvalue + 1

    def zero(self):
        return 0

    def negative_value(self):
        return (-1)

    def fractional_value(self):
        return 1.5

    def generator(self):
        if self.type in ('int32', 'int64'):
            print(f'"{self.name}" : "{self.empty_string()}"')
            print(f'"{self.name}" : "{self.space()}"')
            print(f'"{self.name}" : {self.none()}')
            print(f'"{self.name}" : "{self.digits_string()}"')
            print(f'"{self.name}" : "{self.latin_string()}"')
            print(f'"{self.name}" : "{self.cyrillic_string()}"')
            print(f'"{self.name}" : {self.fractional_value()}')
            print(f'"{self.name}" : {self.min_value()}')
            print(f'"{self.name}" : {self.max_value()}')
            print(f'"{self.name}" : {self.greater_than_max_value()}')
            print(f'"{self.name}" : {self.less_than_min_value()}')
            print(f'"{self.name}" : {self.zero()}')
            # print(f'"{self.name}" : "{self.negative_value()}"')
            print(f'"{self.name}" : {self.fractional_value()}')


class String(Parameter):
    def __init__(self, name, required, maxlength=150, type='string', included_list=None, excluded_list=None):
        Parameter.__init__(self, name, type, required)
        self.excluded_list = excluded_list
        self.included_list = included_list
        self.maxlength = maxlength

    # @staticmethod
    # def cyrillic_uppercase():
    #     cyrillic_list = []
    #     for i in range(1040, 1072):
    #         cyrillic_list.append(chr(i))
    #     return cyrillic_list
    #
    # @staticmethod
    # def cyrillic_lowercase():
    #     cyrillic_list = []
    #     for i in range(1072, 1104):
    #         cyrillic_list.append(chr(i))
    #     return cyrillic_list

    def digits_string(self):
        return rstr.rstr(string.digits, start_range=1, end_range=min(10, self.maxlength))

    def latin_string(self):
        return rstr.rstr(string.ascii_letters, start_range=1, end_range=min(10, self.maxlength))

    def string_of_given_chars(self, chars_list):
        return rstr.rstr(chars_list, start_range=1, end_range=min(10, self.maxlength))

    def cyrillic_string(self):
        cyrillic_string = ''
        for i in range(1040, 1104):
            cyrillic_string += str(chr(i))
        return rstr.rstr(cyrillic_string, start_range=1, end_range=min(10, self.maxlength))

    def special_chars_string(self):
        return "?!"

    def generate_positive(self):
        pass


class Generator:
    def __init__(self, params_list=None, mandatory_params_list=None):
        if params_list is None:
            self.params_list = []
        else:
            self.params_list = params_list
        if mandatory_params_list is None:
            self.mandatory_params_list = []
            for item in self.params_list:
                if item.required:
                    self.mandatory_parameters_list.append(item)
        else:
            self.mandatory_parameters_list = mandatory_params_list

    def add_to_params_list(self, param):
        self.params_list.append(param)

    def print_params_list(self):
        for item in self.params_list:
            item.print_parameter()

    def all_parameters_text_digits(self):
        for item in self.params_list:
            pass

    def mandatory_parameters(self):
        required_params = []
        i = 1
        dict = {}
        for item in self.params_list:
            if item.required:
                required_params.append(item)
                if item.type in ('int32', 'int64'):
                    dict[item.name] = i
                    i += 1
        return required_params

    # TODO: добавить работу с паттернами
    def text_latin(self):
        dict = {}
        for item in self.params_list:
            if item.type == 'string':
                dict[item.name] = item.latin_string()
        print(dict)
        return dict

    def text_cyrillic(self):
        dict = {}
        for item in self.params_list:
            if item.type == 'string':
                dict[item.name] = item.cyrillic_string()
        return dict

    def text_special_symbols(self):
        pass
