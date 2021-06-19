# randomizervk
<h1> Рандомайзер для определения победителя вашего розыгрыша.</h1>




<p align="center">Для корректной работы бота установите самую последнюю версию python.
  
### Установка:
```sh
git clone https://github.com/l1v0n1/randomizervk.git

cd randomizervk

pip install -r requirements.txt
```
### Настройка(main.py):

```sh
bot = Bot(
	"123", # вместо 123 вставляем токен от вашей группы вконтакте
	group_id=123, # id группы, без минуса
)

api = API("123") # вставляем токен от вашей страницы вк
```

### Запускаем
```sh
python main.py
```
