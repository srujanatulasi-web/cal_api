from fastapi import FastAPI, Request
app = FastAPI()


@app.get("/add")
def add(request: Request):
    value1 = request.query_params.get('a')
    value2 = request.query_params.get('b')
    return int(value1) + int(value2)
 
@app.get("/sub")
def sub(request: Request):
    value1 = request.query_params.get('a')
    value2 = request.query_params.get('b')
    return int(value1) - int(value2)
 
@app.get("/mul")
def mul(request: Request):
    value1 = request.query_params.get('a')
    value2 = request.query_params.get('b')
    return int(value1) * int(value2)
 
@app.get("/div")
def div(request: Request):
    value1 = request.query_params.get('a')
    value2 = request.query_params.get('b')
    return int(value1) / int(value2)
 
@app.get("/exp")
def exp(request: Request):
    value1 = request.query_params.get('a')
    value2 = request.query_params.get('b')
    return int(value1) ** int(value2)
 
@app.get("/floor_div")
def floor_div(request: Request):
    value1 = request.query_params.get('a')
    value2 = request.query_params.get('b')
    return int(value1) // int(value2)