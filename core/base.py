"""
core.base -- базовые классы
Create at 26.01.2023 15:59:16
~/core/base.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2022'
__license__ = 'KIB'
__credits__ = [
    'pavelmstu',
]
__version__ = "20230126"
__status__ = "Production"

from typing import Optional

from Crypto.Cipher import AES

Link = str
Message = str
Key = str


class BaseSdarn:
    """
    self-destruct after being read notes.
    """
    # базовый урл.
    _base_url = None

    @classmethod
    def check(cls):
        """
        Проверка что cls._base_url доступен
        :return:
        """
        return NotImplemented

    @classmethod
    def max_length(cls):
        """
        возвращает максимальную длину возможного записываемого сообщения
        без учёта перевода в base64
        :return:
        """
        return NotImplemented

    @classmethod
    def raw_write(cls, row_message: Message) -> Link:
        """
        Запись сообщения row_message и получения ссылки
        :param row_message:
        :return:
        """
        return NotImplemented

    @classmethod
    def check_read(cls, link: Link) -> bool:
        """
        вернуть True, если по указанной ссылке есть сообщение.
        :param link:
        :return:
        """
        return NotImplemented

    @classmethod
    def raw_read(cls, link: Link) -> Optional[Message]:
        """
        Прочитать сообщение по ссылке,
        или вернуть None, если его нет
        :param link:
        :return:
        """
        return NotImplemented

    @classmethod
    def write(cls, message: Message, key: Key) -> Link:

        # TODO
        #  1. проверить по cls.max_length (с учётом дальнейшей поправки на base64)
        #  2. шифрануть
        #  3. взять base64
        #. 4. вызвать

        raise NotImplementedError()
        row_message = 'TODO'
        return cls.raw_write(row_message)

    @classmethod
    def read(cls, link: Link, key: Key) -> Message:
        assert isinstance(cls._base_url, str)
        assert link.startswith(cls._base_url)

        # TODO
        #   ??? обратный процесс write
        if not cls.check_read(link):
            raise Exception(f"По ссылке {link} нет сообщения. Либо оно уже было прочитано")
        raw_message = cls.raw_read(link)
        pass
        #   ----------------------------------------------------------------------------------------------------------
        raise NotImplementedError()
        message = "TODO"
        return message