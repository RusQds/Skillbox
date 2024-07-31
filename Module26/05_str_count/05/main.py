import os
from collections.abc import Iterable


def count_lines(path: str) -> Iterable[str]:
    for dir_elem in os.listdir(path):
        if os.path.isfile(dir_elem) and dir_elem.endswith('.py'):
            with open(os.path.join(path, dir_elem), 'r', encoding='utf-8') as lines:
                for line in lines:
                    if not line.startswith('#') and not line.startswith('\n') and len(line) > 0:
                        print(os.path.join(path, dir_elem))
                        yield len(line)


now_path = os.path.join(os.path.abspath(''))
for count in count_lines(now_path):
    print(count)
