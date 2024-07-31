import os
from collections.abc import Iterable


def gen_files_path(my_dir='C:\\') -> Iterable[str]:
    path = os.path.abspath(my_dir)
    for path_elem in os.listdir(path):
        new_path = os.path.join(path, path_elem)
        if os.path.isfile(new_path):
            yield new_path


my_path = gen_files_path(my_dir='C:\\')
for elem in my_path:
    print(elem)
