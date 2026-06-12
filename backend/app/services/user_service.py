from backend.app.models.user import User


USERS = {

    "admin": {
        "role": "admin"
    },

    "hr_user": {
        "role": "HR"
    },

    "finance_user": {
        "role": "Finance"
    },

    "employee_user": {
        "role": "employee"
    }
}


def get_user(
    username
):

    data = USERS.get(
        username
    )

    if not data:

        return None

    return User(

        username=username,

        role=data["role"]
    )