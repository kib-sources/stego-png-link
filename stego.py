"""
Основной запускаемый файл.

>> stego png-link --help

Ю


Create at 26.01.2023 15:32:47
~//stego.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2022'
__license__ = 'KIB'
__credits__ = [
    'pavelmstu',
]
__version__ = "20230126"
__status__ = 'Develop'  # "Production"

import os

import argparse

FOLDER_EMPTY_CONTAINERS = './empty_containers'
FLAG_DONOR = '--donor'

# TODO исследовать и дополнить список
DONOR_TYPES = [
    '.avi',
    '.mkv',
]


'''
parser = argparse.ArgumentParser(
    prog='KIB stego programs. See https://github.com/orgs/kib-sources/repositories?q=stego',
    description='Программа для стеганографии',
    epilog='Text at the bottom of help',
)
# '''

parser = argparse.ArgumentParser(
    prog='stego-png-link',
    description="Описание программы",
    epilog="Конец описания программы",
)

# TODO
#   https://docs.google.com/document/d/1LQot8bpHgHo4TZXKlswronbxIpmF58S7s-FLfSLnAFU
# parser.add_argument(
# )

parser.add_argument(
    '--generate_empty_containers',
    dest='count_generate_empty_containers',
    default=None,
    help=f'Сколько сгенерировать новых PNG пустых контейнеров и поместить их в папку {FOLDER_EMPTY_CONTAINERS}. Важно: необходим флаг {FLAG_DONOR}'
)

parser.add_argument(
    FLAG_DONOR,
    dest='donor_path',
    default=None,
    help=f'Путь к донору типа {",".join(DONOR_TYPES)}. Если нет флага --generate_empty_containers, то игнорируется.'
)


def generate_empty_containers(donor_path: str, count: int, out_folder=FOLDER_EMPTY_CONTAINERS):
    """
    Помещает
    :param donor_path:
    :param out_folder:
    :param count: сколько случайных изображений будет выцарапано
    :return:
    """
    return NotImplemented


def check():
    """
    Проверка стего-окружения.
    А именно:
    Доступность
        1. https://privnote.com/
        2. https://clck.ru/
        3. Наличие свободных PNG сообщений в папке pngs
        4. установленные тулзы из requirements.txt, в частности ffmpeg
    :return:
    """
    return NotImplemented


def main(args):
    return NotImplemented


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)

