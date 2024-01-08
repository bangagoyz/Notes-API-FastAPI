import motor.motor_asyncio

MONGODB_URL = "YOUR MONGODB LINK"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.notes_db