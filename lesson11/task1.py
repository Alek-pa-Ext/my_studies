import threading, json, random, os


def create_json():
    cur_dir = os.getcwd()
    json_path = os.path.join(cur_dir, 'numbers.json')
    with open(json_path, 'w') as json_file:
        json.dump([random.randint(-100, 100) for _ in range(100)], json_file)
    return json_path


def load_data(json_path):
    with open(json_path, 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data


def put_data(json_path, data):
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file)
    print('Write in ', json_file)


def data_proc(data, setting):
    if setting == 'positive':
        result_data = [num for num in data if  num >= 0]
    elif setting == 'negative':
        result_data = [num for num in data if num < 0]
    else:
        result_data = 'error'
    print(result_data)
    return result_data


def program(json_path):
    numbers_list = load_data(json_path)
    dir_name = os.path.dirname(json_path)
    print(numbers_list)
    positive_thread = threading.Thread(target=put_data, args=(os.path.join(dir_name, 'positive.json'),
                                                                data_proc(numbers_list, 'positive')))
    negative_thread = threading.Thread(target=put_data, args=(os.path.join(dir_name, 'negative.json'),
                                                                data_proc(numbers_list, 'negative')))

    positive_thread.start()
    print('positive_thread is start')
    negative_thread.start()
    print('negative_thread is start')
    positive_thread.join()
    print('positive_thread is end')
    negative_thread.join()
    print('negative_thread is end')


def check_results(json_path):
    dir_name = os.path.dirname(json_path)
    start_data = set(load_data(json_path))
    result_data = set(load_data(os.path.join(dir_name, 'positive.json')) +
                      load_data(os.path.join(dir_name, 'negative.json')))
    print(set.difference(start_data, result_data) or 'No errors')

if __name__ == '__main__':
    json_path = create_json()

    program(json_path)
    check_results(json_path)
