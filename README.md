# pythio
A library for bot development in Telegram messengers

# Example
```python
from pythio import Client
import asyncio


client = Client('YOUR_TOKEN_HERE')

async def main():
    async for message in client.on_message():
        print(message.text)
        await message.reply('Hello World!')


if __name__ == '__main__':
    asyncio.run(main())

```

## Documents
- [Telegram Channel](https://t.me/pythio)
