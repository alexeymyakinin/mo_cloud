from server.src.schemas import Schema


class UserSchema(Schema):
    username: str


class UserSchemaDB(UserSchema):
    id: int
