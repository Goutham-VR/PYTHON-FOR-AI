#itrator
import asyncio
class Number:
    def __aiter__(self):
        self.number=0
        return self
    async def __anext__(self):
        if self.number>3:
            raise StopAsyncIteration
        value=self.number
        self.number+=1

        await asyncio.sleep(1)
        return value

async def main():
    async for number in Number():
        print(number)

asyncio.run(main())