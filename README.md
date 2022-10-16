# Тестовое задание на Python разработчика для Exo World

## Первое задание
- MainGame.py: его запускать, в нем построена вся игра.
- Wolf.py: там описан класс Wolf (волка), нужные функции для работы с волками в игре.
- Horse.py: там описан класс Horse (коня), нужные функции для работы с конем.
- Officer.py: там описан класс Officer (офицер), нужные функции для работы с офицером.
- Как играть: поочередно происходит считывание данных с клавиатуры: сначала координата x, потом y ячейки, куда нужно передвинуть офицера, если это попытка атаковать волка, и выполнены все для этого условия, то происходит атака, иначе происходит ход, если не выполнены какие-то условия, то вылезает уведомление об этом, и координаты надо ввести снова. Дальше тоже самое, только для коня, после чего присылается обновленная доска, и цикл повторяется до тех пор, пока все волки не будут убиты.

## Второе задание
- необходимо установить Pillow!
- ttoken.txt: содержит токен для Telegram бота
- TBot.py: телеграм бот
- Image.py: там функционал для работы с изображением
- Cat.jpg: изобрвжение кота
- Как использовать: в token.txt вместо secret нужно поместить токен своего Telegram бота, дальше запустить TBot.py, при отправке боту сообщения /start пользователь получит изображение кота, поверх которого будет помещен текст, содержащий время и дату отправки сообщения.
