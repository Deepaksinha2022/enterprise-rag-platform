from fastapi import APIRouter

from backend.app.services.user_service import (
    get_user
)

from backend.app.auth.jwt_handler import (
    create_token
)

router = APIRouter()


@router.post("/login")
async def login(
    username: str
):

    user = get_user(
        username
    )

    if not user:

        return {
            "error": "User not found"
        }

    token = create_token(
        username
    )

    return {
        "access_token": token
    }

from fastapi import Header

@router.get("/test-header")
async def test_header(
    authorization: str = Header(...)
):
    return {
        "header": authorization
    }