from fastapi import FastAPI
app = FastAPI()


@app.get('/')
async def root():
    return {'status': 200, 'data': [], 'message': 'API route with V-1', 'app': 'FastAPI-Learn', 'version': 'basic'}


@app.get('/api/v1/')
async def root():
    return {'status': 200, 'data': [], 'message': 'API route with V-1', 'app': 'FastAPI-Learn', 'version': '1.0'}
