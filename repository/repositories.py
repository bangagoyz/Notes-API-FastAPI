from models.notes import Note
from config.databases import database
import datetime
import uuid

class NoteRepo():

    @staticmethod
    async def retrieve():
        _note = []
        collection = database.get_collection('note').find()
        async for note in collection:
            _note.append(note)
        return _note
    
    @staticmethod
    async def insert(note:Note):
        id = str(uuid.uuid4())
        createdAt = datetime.datetime.now()
        _note = {
            "_id": id,
            "title":note.title,
            "content": note.content,
            "createdAt": createdAt
        }
        await database.get_collection('note').insert_one(_note)
        return _note

    @staticmethod
    async def update(id: str, note: Note):
        _note = await database.get_collection('note').find_one({"_id": id})
        _note["title"] = note.title
        _note["content"] = note.content
        _note["updatedAt"] = datetime.datetime.now()
        await database.get_collection('note').update_one({"_id":id}, {"$set":_note})
        return _note

    @staticmethod
    async def retireve_id(id:str):
        return await database.get_collection('note').find_one({"_id":id})
    
    @staticmethod
    async def delete(id:str):
        await database.get_collection('note').delete_one({"_id": id})
        return True