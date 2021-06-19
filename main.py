from vkbottle import Bot, Message, VKError
from vkbottle.api import API
import random

bot = Bot(
	"123", # токен от группы
	group_id=123, # id группы, без минуса
)

api = API("123") # токен от вашей страницы

@bot.on.message()
async def handler(message: Message):
	if 'vk.com' in message.text:
		h = message.text.split('wall')
		all = h[1]
		i = all.split('_')
		id = i[0]
		item = i[1]
		try:
			# победитель по лайкам
			req = await api.request("likes.getList", {"type": "post", "owner_id": id, "item_id": item})
			count = req['count']
			tox = req['items']
			choice = random.choice(tox)
			link = f"vk.com/id{choice}"
			await message(f'Ваш Победитель выявлен честной системой рандома:\nКоличество лайкнувших пост: {count}\nПобедитель: {link}')
		except Exception as error:
			await message('Ошибка, возможно вы ввели неверно ссылку или на записи нет лайков.')
	else:
		await message('Привет, хочешь узнать победителя своего розыгрыша?\nПросто отправь мне ссылку на пост.')

bot.run_polling()