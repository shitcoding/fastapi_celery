from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get('/')
    async def root():
        return {'message': 'Well hello motherfucka'}

    return app
