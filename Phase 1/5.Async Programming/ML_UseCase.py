import asyncio
async def download_model():
    ...

async def load_database():
    ...

async def main():

    model_task = asyncio.create_task(download_model())

    # Do something else while model downloads
    await load_database()

    model = await model_task