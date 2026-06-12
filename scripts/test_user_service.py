from backend.app.services.user_service import (
    get_user
)

user = get_user(
    "finance_user"
)

print(user)

print(
    user.can_access_department(
        "Finance"
    )
)

print(
    user.can_access_department(
        "HR"
    )
)