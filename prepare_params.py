from model.parameter import String
from model.parameter import Number
from model.parameter import Generator
import json

with open('input.json', 'r') as f:
    data = json.load(f)
    print(type(data))
    list_of_params = Generator()
    for key, value in data[[*data][0]]['properties'].items():
        if value['type'] == 'string':
            param = String(name=key, type=value['type'], required=key in data[[*data][0]]['required'])
        elif value['type'] == 'integer':
            param = Number(name=key, type=value['format'], required=key in data[[*data][0]]['required'])
        else:
            pass
        list_of_params.add_to_params_list(param)
    # list_of_params.print_params_list()
        # param.print_parameter()
        # param.generator()
    # list_of_params.mandatory_parameters()
    list_of_params.text_latin()
