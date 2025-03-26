import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from unittest.mock import AsyncMock, Mock

from src.entity.models import Todo, User
from src.repositories.todos_repository import TodoRepository
from src.schemas.todo import TodoSchema, TodoUpdateSchema, TodoUpdateStatusSchema

@pytest.fixture
def mock_session():
    session = AsyncMock(spec=AsyncSession)
    # session.execute = AsyncMock()
    # session.commit = AsyncMock()
    # session.refresh = AsyncMock()
    # session.add = Mock()
    # session.delete = AsyncMock()
    return session

@pytest.fixture
def mock_user():
    return User(id=1, username="test_user")

@pytest.fixture
def todos_repository(mock_session):
    return TodoRepository(mock_session)

@pytest.mark.asyncio
async def test_get_todos(todos_repository, mock_session, mock_user):
    # Arrange
    limit = 10
    offset = 0
    mock_todos = [Todo(id=1, title="Test Todo"), Todo(id=2, title="Another Todo")]
    mock_result = Mock()
    mock_result.scalars.return_value.all.return_value = mock_todos
    mock_session.execute.return_value = mock_result

    # Act
    result = await todos_repository.get_todos(limit, offset, mock_user)

    # Assert
    assert result == mock_todos
    mock_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_get_todo_by_id(todos_repository, mock_session, mock_user):
    # Arrange
    todo_id = 1
    mock_todo = Todo(id=todo_id, title="Test Todo")
    mock_result = Mock()
    mock_result.scalar_one_or_none.return_value = mock_todo
    mock_session.execute.return_value = mock_result

    # Act
    result = await todos_repository.get_todo_by_id(todo_id, mock_user)

    # Assert
    assert result == mock_todo
    mock_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_create_todo(todos_repository, mock_session, mock_user):
    # Arrange
    todo_data = TodoSchema(title="New Todo", description="Test Description")
    mock_todo = Todo(
        id=1,
        title=todo_data.title,
        description=todo_data.description,
        user_id=mock_user.id
    )

    async def mock_refresh(todo):
        return mock_todo


    mock_session.refresh.side_effect = mock_refresh


    # Act
    result = await todos_repository.create_todo(todo_data, mock_user)

    # Assert
    assert result.title == mock_todo.title
    assert result.description == mock_todo.description
    assert result.user_id == mock_todo.user_id
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()

@pytest.mark.asyncio
async def test_remove_todo(todos_repository, mock_session, mock_user):
    # Arrange
    todo_id = 1
    mock_todo = Todo(id=todo_id, title="Test Todo")
    mock_result = Mock()
    mock_result.scalar_one_or_none.return_value = mock_todo
    mock_session.execute.return_value = mock_result

    # Act
    result = await todos_repository.remove_todo(todo_id, mock_user)

    # Assert
    assert result == mock_todo
    mock_session.delete.assert_called_once_with(mock_todo)
    mock_session.commit.assert_called_once()

@pytest.mark.asyncio
async def test_update_todo(todos_repository, mock_session, mock_user):
    # Arrange
    todo_id = 1
    update_data = TodoUpdateSchema(title="Updated Todo")
    mock_todo = Todo(id=todo_id, title="Old Title")
    mock_result = Mock()
    mock_result.scalar_one_or_none.return_value = mock_todo
    mock_session.execute.return_value = mock_result
    mock_session.refresh.return_value = mock_todo

    # Act
    result = await todos_repository.update_todo(todo_id, update_data, mock_user)

    # Assert
    assert result.title == "Updated Todo"
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()

@pytest.mark.asyncio
async def test_update_todo_status(todos_repository, mock_session, mock_user):
    # Arrange
    todo_id = 1
    update_data = TodoUpdateStatusSchema(completed=True)
    mock_todo = Todo(id=todo_id, completed=False)
    mock_result = Mock()
    mock_result.scalar_one_or_none.return_value = mock_todo
    mock_session.execute.return_value = mock_result
    mock_session.refresh.return_value = mock_todo

    # Act
    result = await todos_repository.update_todo(todo_id, update_data, mock_user)

    # Assert
    assert result.completed is True
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once() 