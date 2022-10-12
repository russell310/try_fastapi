import strawberry
from fastapi import FastAPI
from project.database import init_db
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from project.mutations import Mutation
from project.queries import Query

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))


def create_app() -> FastAPI:
    app = FastAPI()
    graphql_app = GraphQLRouter(schema)

    @app.on_event("startup")
    async def startup_event():
        init_db(app)

    app.include_router(graphql_app, prefix="/graphql")

    return app
