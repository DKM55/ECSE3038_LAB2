from fastapi import FastAPI

app = FastAPI()

data = [
    {
        "name": "Beef Wellington",
        "occupation": "Fry Cook",
        "address": "124 Conch Street"
    }
]

@app.post("/person")
def add_person(person):
    if person.name and person.occupation and person.address:
        data.append(person.dict())
    
        return {"success": True, "result": person.dict()}
    else:

        return{"success":False,"error_message":"Invalid request"},

@app.get("/person")
def get_person():
    return data

