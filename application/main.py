
# import typing and its modules
from typing import Optional
# Importing FastAPI
#from fastapi import FastAPI

# app = FastAPI()  # Creating instance
from application import app


@app.get('/')
async def api():
    return {'status': 200, 'data': [], 'message': 'API route with V-1', 'app': 'FastAPI-Learn', 'version': 'basic'}


@app.get('/api/v1/')
async def staticVersion(v: str):
    return {'status': 200, 'data': [], 'message': 'API route with V-1', 'app': 'FastAPI-Learn', 'version': '1.0'}


@app.get('/api/{v}/')
async def dynamicVersion(v: str):
    return {'status': 200, 'data': [], 'message': 'API route with ' + v, 'app': 'FastAPI-Learn', 'version': v}


@app.get('/api/v1/pages')
async def staticVersionPages():
    return {'status': 200, 'data': [
        {"id": 1, "title": "Home"},
        {"id": 2, "title": "About"},
        {"id": 3, "title": "Contact"}
    ], 'message': 'Pages', 'app': 'FastAPI-Learn', 'version': '1.0'}


@app.get('/api/v1/pages')
async def staticVersionPages(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return {'status': 200, 'data': [
        {"id": 1, "title": "Home"},
        {"id": 2, "title": "About"},
        {"id": 3, "title": "Contact"}
    ], 'message': 'Pages', 'app': 'FastAPI-Learn', 'version': '1.0'}


@ app.get('/api/{v}/pages')
async def dynamicVersionPages(v: str):
    return {'status': 200, 'data': [
        {"id": 1, "title": "Home"},
        {"id": 2, "title": "About"},
        {"id": 3, "title": "Contact"}
    ], 'message': 'Pages', 'app': 'FastAPI-Learn', 'version': v}


@ app.get('/api/v1/page/details/{id}')
async def staticVersionPagedDetails(id: int):
    return {'status': 200, 'data':
            {
                "id": id,
                "title": "Home",
                "description": "This is a home page"
            },
            'message': 'Page details', 'app': 'FastAPI-Learn', 'version': '1.0'}


@ app.get('/api/{v}/page/details/{id}')
async def dynamicVersionPagedDetails(v: str, id: int):
    return {'status': 200, 'data':
            {
                "id": id,
                "title": "Home",
                "description": "This is a home page"
            },
            'message': 'Page details', 'app': 'FastAPI-Learn', 'version': v}
