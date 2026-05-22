from fastapi import FastAPI
app= FastAPI()

@app.get("/")
def get_details():
    return{
        "message":"Welcom to the New World!"
    }