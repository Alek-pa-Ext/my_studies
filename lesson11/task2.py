import json, random, os, logging
from multiprocessing import Process


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
    logging.info('Write in ', json_path)

def negative(data):
    result_data = [num for num in data if num < 0]
    put_data(os.path.join(os.getcwd(), 'negative.json'), result_data)
    logging.info('Function negative done')


def positive(data):
    result_data = [num for num in data if num >= 0]
    put_data(os.path.join(os.getcwd(), 'positive.json'), result_data)
    logging.info('Function positive done')


def program(json_path):
    numbers_list = load_data(json_path)
    logging.info(numbers_list)
    positive_proc = Process(target=positive, args=(numbers_list,))
    negative_proc =Process(target=negative, args=(numbers_list,))

    positive_proc.start()
    logging.info('positive_proc is start')
    negative_proc.start()
    logging.info('negative_proc is start')
    positive_proc.join()
    logging.info('positive_proc is end')
    negative_proc.join()
    logging.info('negative_proc is end')


def check_results(json_path):
    dir_name = os.path.dirname(json_path)
    start_data = set(load_data(json_path))
    result_data = set(load_data(os.path.join(dir_name, 'positive.json')) +
                      load_data(os.path.join(dir_name, 'negative.json')))
    logging.info(set.difference(start_data, result_data) or 'No errors')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    json_path = create_json()

    program(json_path)
    check_results(json_path)
