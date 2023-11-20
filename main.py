from fastapi import FastAPI
app = FastAPI() #instantiate app

#setup route
@app.get("/")
async def root():
    return {"message": "hello world"}
@app.post("/")
async def post():
    return {"message": "hello from the post route"}
@app.put("/")
async def put():
    return{"message":"hey from put route uWu"}
@app.get("/items")
async def list_items():
    return{"message":"list items"}
@app.get("/items/{item_id}")
async def get_item(item_id:int):
    return{"item_id":item_id}