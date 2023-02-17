"""
Proof Of Consept для записи и чтения зашифрованного сообщения посредством записи в метаданных PNG файла.

Программа использует метод XOR-шифрования для защиты текста. Для шифрования текста необходимо ввести ключ, который используется вместе с оператором XOR для преобразования символов текста в зашифрованные символы. Расшифровка текста осуществляется также с помощью ключа и оператора XOR.
После шифрования текста, программа создает новый PNG файл, добавляет в его метаданные комментарий с зашифрованным текстом и записывает этот файл на диск. Зашифрованный текст можно потом извлечь из метаданных PNG файла и расшифровать обратно.
Программа реализована на языке Python и не использует сторонних библиотек для работы с PNG файлами. Пользовательский интерфейс программы реализован через командную строку.
Пример работы смотреть в poc\README.md
Create at 13.02.2023 00:00:00
~/poc/comment_png_poc.py
"""

import sys

__author__ = 'tunderof'
__copyright__ = 'KIB, 2023'
__credits__ = [
    'tunderof'
]

__license__ = 'LGPL'
__version__ = "20230213"
__status__ = "Production"


def write(message, output_file):
    with open(file_examaple, "rb") as f:
        original_image = f.read()

    # Разделение файла на чанки
    chunks = []
    chunk_start = 8 # Пропуск 8 байт данных, для игнорирования сигнатуры PNG файла
    while chunk_start < len(original_image):
        chunk_length = int.from_bytes(original_image[chunk_start:chunk_start+4], "big")
        chunk_type = original_image[chunk_start+4:chunk_start+8].decode()
        chunk_data = original_image[chunk_start+8:chunk_start+8+chunk_length]
        chunk_crc = original_image[chunk_start+8+chunk_length:chunk_start+12+chunk_length]
        chunks.append((chunk_type, chunk_data, chunk_crc))
        # 12 -- это число, которое отвечает за пропуск 4 байт длины чанка, 4 байт названия чанка, 4 байт значения CRC алгоритма
        chunk_start += 12 + chunk_length

    # Генерация Comment чанка
    comment_chunk = generate_comment_chunk(message)
    # Add the comment chunk to the list of chunks
    chunks = [("IHDR", chunks[0][1], chunks[0][2])] + [comment_chunk] + chunks[1:]

    # Генерация нового изображения
    png_signature = b"\x89PNG\r\n\x1a\n"
    new_image = png_signature # Создание переменной для хранения данных генерируемого изображения
    for chunk_type, chunk_data, chunk_crc in chunks:
        chunk = (len(chunk_data)).to_bytes(4, "big") + chunk_type.encode() + chunk_data + chunk_crc
        new_image += chunk

    #Запись в новый файл
    with open(output_file, "wb") as f:
        f.write(new_image)


def generate_comment_chunk(comment):
    #tEXt -- Чанк для хранения текстовых строк.
    #https://www.w3.org/TR/2003/REC-PNG-20031110/#11tEXt
    chunk_type = "tEXt"
    chunk_data = f"Comment\0{comment}".encode()
    chunk_crc = 0
    for b in chunk_type.encode():
        chunk_crc = (chunk_crc * 256 + b) % (2**32)
    for b in chunk_data:
        chunk_crc = (chunk_crc * 256 + b) % (2**32)
    chunk_crc = (chunk_crc ^ 0xFFFFFFFF) % (2**32)
    chunk = (chunk_type, chunk_data, chunk_crc.to_bytes(4, "big"))
    return chunk


def read(input_file):
    with open(input_file, "rb") as f:
        data = f.read()
        start_pos = data.find(b'tEXtComment')
        chunk_length = int.from_bytes(data[start_pos - 4:start_pos], 'big')
        chank_end = start_pos + chunk_length + 8
        chunk_data = data[start_pos + 12:chank_end - 4] # -4 = crc; +12 = tEXtComment с пробелом
        print(f"MESSAGE: {decrypt(chunk_data, crypt_key)}")
        #print(chunk_data)


def encrypt(text, key):
    encrypted_text = ""
    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(encrypted_text, key):
    text = ""
    for i, char in enumerate(encrypted_text):
        key_char = key[i % len(key)]
        decrypted_char = chr(char ^ ord(key_char))
        text += decrypted_char
    return text


if __name__ == "__main__":
    file_examaple = 'input1.png' #Дефолт значение
    crypt_key = 'secr_123t'
    try:
        op_mode = sys.argv[1]
        if op_mode == '--em':
            message = encrypt(text=sys.argv[2], key=crypt_key)
            #message = sys.argv[2]
            if sys.argv[3] == '--out':
                output_file = sys.argv[4]
                write(message=message, output_file=output_file)
        elif op_mode == '--ex':
            if sys.argv[2] == '--in':
                input_file = sys.argv[3]
                read(input_file=input_file)
    except IndexError:
        raise Exception("Ошибка чтения аргументов")