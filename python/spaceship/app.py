from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from typing import List, Dict
import numpy as np

from spaceship.config import Settings
from spaceship.routers import api, health


def make_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        debug=settings.debug,
        title=settings.app_title,
        description=settings.app_description,
        version=settings.app_version,
    )
    app.state.settings = settings

    if settings.debug:
        app.mount('/static', StaticFiles(directory='build'), name='static')

    app.include_router(api.router, prefix='/api', tags=['api'])
    app.include_router(health.router, prefix='/health', tags=['health'])

    @app.get('/', include_in_schema=False, response_class=FileResponse)
    async def root() -> str:
        return 'build/index.html'

    @app.get('/matrix/', response_model=Dict[str, List[List[float]]])
    async def multiply_matrices_endpoint(rows1: int = 10, cols1: int = 10, rows2: int = 10, cols2: int = 10):
        matrix1 = np.random.rand(rows1, cols1)
        matrix2 = np.random.rand(rows2, cols2)
        result = np.dot(matrix1, matrix2)
        return {
            'matrix_a': matrix1.tolist(),
            'matrix_b': matrix2.tolist(),
            'result': result.tolist()
        }

    return app