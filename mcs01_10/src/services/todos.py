from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import User
from src.repositories.todos_repository import TodoRepository
from src.schemas.todo import TodoSchema, TodoUpdateSchema, TodoUpdateStatusSchema


class TodoService:
    def __init__(self, db: AsyncSession):
        self.todo_repository = TodoRepository(db)

    async def create_todo(self, body: TodoSchema, user: User):
        return await self.todo_repository.create_todo(body, user)

    async def get_todos(self, limit: int, offset: int, user: User):
        return await self.todo_repository.get_todos(limit, offset, user)

    async def get_todo(self, todo_id: int, user: User):
        return await self.todo_repository.get_todo_by_id(todo_id, user)

    async def update_todo(self, todo_id: int, body: TodoUpdateSchema, user: User):
        return await self.todo_repository.update_todo(todo_id, body, user)

    async def update_status_todo(
        self, todo_id: int, body: TodoUpdateStatusSchema, user: User
    ):
        return await self.todo_repository.update_todo(todo_id, body, user)

    async def remove_todo(self, todo_id: int, user: User):
        return await self.todo_repository.remove_todo(todo_id, user)
