import uvicorn

if __name__ == '__main__':
    '''
    uvicorn.run(
        app="application.main:app",
        host="127.0.0.1",
        port=9990,
        reload=True
    )
    '''
    uvicorn.run(
        app="notes.app:app",
        host="127.0.0.1",
        port=9990,
        reload=True
    )
