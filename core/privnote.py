"""


Create at 26.01.2023 16:15:35
~/core/privnote.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2022'
__license__ = 'KIB'  # TODO
__credits__ = [
    'pavelmstu',
]
__version__ = "20230126"
__status__ = 'Develop'  # "Production"


from typing import Optional

from core.base import Link, Message
from core.base import BaseSdarn


class PrivnoteSdarn(BaseSdarn):

    _base_url = 'https://privnote.com/'

    @classmethod
    def raw_write(cls, row_message: Message) -> Link:
        """
        Запись сообщения row_message и получения ссылки
        :param row_message:
        :return:
        """
        raise NotImplementedError()

    @classmethod
    def check_read(cls, link: Link) -> bool:
        """
        вернуть True, если по указанной ссылке есть сообщение.
        :param link:
        :return:
        """
        raise NotImplementedError()

    @classmethod
    def raw_read(cls, link: Link) -> Optional[Message]:
        """
        Прочитать сообщение по ссылке,
        или вернуть None, если его нет
        :param link:
        :return:
        """
        raise NotImplementedError()
