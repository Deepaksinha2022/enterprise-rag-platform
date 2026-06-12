# scripts/test_admin_access.py

from backend.app.services.user_service import (
    get_user
)

user = get_user(
    "admin"
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

print(
    user.can_access_department(
        "Compliance"
    )
)