import json

def create_class_from_dict(dictionary: dict, class_name: str) -> str:
    ret = f'class {class_name}:\n'
    doc_str_params = '    """\n'
    doc_str_types = ''
    init_str = '    def __init__(self,\n'
    init_content_str = '        super().__init__(**kwargs)\n'

    for key, value in dictionary.items():
        t = type(value)
        doc_str_params += f'    :param {key}: \n'
        doc_str_types += f'    :type {key}: {t.__name__}\n'
        init_str += f'                 {key}: {t.__name__},\n'
        init_content_str += f'        self.{key} = {key}\n'

        # if t == bool:
        # elif t == int:
        # elif t == str:
        # elif t == list:
        # elif t == dict:

    doc_str_types += '    """\n'
    init_str += '                 **kwargs):\n'

    ret = ret + doc_str_params + doc_str_types + init_str + init_content_str
    return ret




def create_data_classes_from_file(file_path: str, class_name: str):
    with open(file_path) as f:
        data = json.load(f)

    with open('created_classes.py', 'w') as f:
        f.write(create_class_from_dict(data, class_name))



if __name__ == "__main__":
    create_data_classes_from_file('data_file.json', 'Rank')