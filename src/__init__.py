from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    from src.users import users_router

    app.include_router(users_router)

    @app.get('/')
    async def root():
        return {'message': 'Well hello motherfucka'}

    return app
