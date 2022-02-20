import glob
import os
import threading
import re
import queue
from itertools import chain


def task1() -> None:
    # в папке test найти все файлы filenames вывести количество
    os.chdir("test/")
    count = 0
    for file_name in glob.glob("**", recursive=True):
        if file_name.endswith('filenames.txt'):
            count += 1
    print('task 1 answer:', count)


def task2() -> None:
    # в папке test найти все email адреса записанные в файлы
    qu = queue.Queue()
    emails = []
    filenames = []
    for file_name in glob.glob('**', recursive=True):
        if file_name.endswith("filenames.txt"):
            filenames.append(file_name)
    threads = [threading.Thread(target=get_email, args=(filenames, qu), daemon=True) for _ in range(5)]
    for thread in threads:
        thread.start()
        response = qu.get()
        emails.append(response)
    for thread in threads:
        thread.join()
    print('task 2 answers:')
    for el in set(list(chain.from_iterable(emails))):
        print(el)


def get_email(filenames: list, queue: queue.Queue = None):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    for file_name in filenames:
        with open(file_name, 'rb') as f:
            text = f.read()
            if text:
                queue.put(re.findall(pattern,  text.decode("utf-8")))


def main():
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()
