from server.src.schemas import Schema


class UserSchema(Schema):
    first_name: str
    last_name: str
    username: str
    email: str
    phone: str


class UserSchemaDB(UserSchema):
    id: int
    hashed_password: str
