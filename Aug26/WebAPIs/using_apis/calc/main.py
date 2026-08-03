import fastapi

api = fastapi.FastAPI()

@api.get('/')
def index():
    return {'msg': 'hello world'}

# add api
@api.get('/add')
def add(a: int, b: int):
    return {'result': a + b}

@api.get('/sub')
def sub(a: int, b: int):
    return {'result': a - b}

@api.get('/mul')
def mul(a: int, b: int):
    return {'result': a * b}

@api.get('/div')
def div(a: int, b: int):
    return {'result': a / b}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(api, host='0.0.0.0', port=8000)