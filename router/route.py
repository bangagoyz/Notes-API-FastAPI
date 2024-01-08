from fastapi import APIRouter, HTTPException
from repository.repositories import NoteRepo
from models.notes import Note, Response


routerr = APIRouter()



@routerr.get("/notes")
async def all_notes():
    _notelist = await NoteRepo.retrieve()
    if _notelist:
        return Response(code=200, status="Ok", message="Success retrieve all data", result=_notelist).dict(exclude_none=True)
    raise HTTPException(404, "There is nothing on here, try to POST one note.")
    

@routerr.post("/notes")
async def create(note: Note):
    _note = await NoteRepo.insert(note)
    if _note:
        return Response(code=200, status="Ok", message="Success save data", result=_note).dict(exclude_none=True)
    raise HTTPException(400, "Something went wrong/ Bad ")


@routerr.get("/notes/{id}")
async def get_note_id(id:str):
    _note =await NoteRepo.retireve_id(id)
    if _note:
        return Response(code=200, status="Ok", message=f"Success retrieve data on id {id}", result=_note).dict(exclude_none=True)
    raise HTTPException(404, f"there is no Note with id {id}")


@routerr.put("/notes/{id}")
async def update(id:str, note:Note):
    _note = await NoteRepo.update(id, note)
    if _note:
        return Response(code=200, status="Ok", message="Success update data", result = _note).dict(exclude_none=True)
    raise HTTPException(404, f"there is no Note with id {id}")
    

@routerr.delete("/notes/{id}")
async def delete(id:str):
    _note =await NoteRepo.delete(id)
    if _note:
        return Response(code=200, status="Ok", message=f"Success delete data with id {id}").dict(exclude_none=True)
    raise HTTPException(404, f"there is no Note with id{id}")