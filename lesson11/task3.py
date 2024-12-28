import json, os, logging, re
from task2 import load_data
from threading import Thread, current_thread

def prog(sample, *args):
    threads = []
    for path in args:
        t = Thread(target=finder, args=(path, sample))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def finder(file_path, sample):
    logger.info(f"Thread '{current_thread().name}' is running")
    text_data = load_data(file_path)['text']
    logger.info(text_data)
    text_data = re.sub(r'[^\w\s]', '', text_data)
    logger.info(text_data)
    data = text_data.lower().split()
    logger.info(data)
    indexes = []
    for i in range(len(data)):
        if data[i] == sample.lower():
            indexes.append(i)
    print(f"In {os.path.basename(file_path)} '{sample}' on this indexes:", indexes)
    logger.info(f"Thread '{current_thread().name}' end the finder")




if __name__ == '__main__':
    logger = logging.getLogger('Test_logger')
    logger.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)

    #json_path1 = input('Enter path to first JSON file: ')
    #json_path2 = input('Enter path to second JSON file: ')
    #word = input('Enter a word to find: ')

    json_path1 = 'task3_file1.json'
    json_path2 = 'task3_file2.json'
    word = 'forest'

    prog(word, json_path1, json_path2)

