from aiogram.utils import executor

import create
from handlers import registration


async def on_startup(_):
	print("Online")


registration.register_client_handlers(dispatcher=create.dp)


if __name__ == "__main__":
	executor.start_polling(create.dp, skip_updates=True, on_startup=on_startup)
