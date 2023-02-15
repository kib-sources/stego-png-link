## Пример работы программы

Переходим в директорию с кодом при помощи команды ```cd poc```.

![ex-poc](https://i.ibb.co/XSLG6Xv/ex-poc.png)

## Запись Hello World в файл
Записывать можно только сообщения на английском языке в формате ASCII

Чтобы записать данные в файл, введем следующую команду:
```bash
~$ python -m comment_png_poc --em <"Ваше сообщение"> --out <*.png>
```
### Пример
![ex-input](https://i.ibb.co/8g9nrp6/ex-input.png)
```bash
~$ python -m comment_png_poc --em "Hello World" --out stego.png
```

## Чтение сообщения из файла
Чтобы получить данные из файла, введите команду:
```bash
~$ python3 -m comment_png_poc --ex --in <*.png>
```
### Пример
![ex-output](https://i.ibb.co/hmyjcZm/ex-output.png)
```bash
~$ python3 -m comment_png_poc --ex --in stego.png
```

