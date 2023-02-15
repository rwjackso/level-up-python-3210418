import json

test_data = {
    'George': {
        'age': 5
    },
    'Susan': {
        'age': 10
    },
    'Mary': {
        'age': 30,
        'kids': ['Susan', 'George']
    }
}


def save_dict(data, file):
    with open(file, 'w') as output_file:
        output_file.write(json.dumps(data))


def restore_dict(file):
    with open(file, 'r') as input_file:
        stored_data = json.load(input_file)

    return stored_data


if __name__ == '__main__':
    print(f'test_data = {test_data}')
    # save_dict(test_data, './mytest.txt')

    restored_data = restore_dict('./mytest.txt')
    print(f'restored_data = {restored_data}')
