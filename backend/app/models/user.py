class User:

    def __init__(
        self,
        username,
        role
    ):

        self.username = username

        self.role = role

    def is_admin(
    self
):

        return (
        self.role
        ==
        "admin"
    )

    def is_hr(
    self
):

        return (
        self.role
        ==
        "hr"
    )


    def is_finance(
    self
):

        return (
        self.role
        ==
        "finance"
    )


    def is_employee(
    self
):

        return (
        self.role
        ==
        "employee"
    )



    def can_access_department(
    self,
    department
):

        if self.is_admin():

            return True

        if (
        self.role
        ==
        department.lower()
    ):

            return True

        return False

    def __str__(self):

        return (
            f"User("
            f"username={self.username}, "
            f"role={self.role}"
            f")"
        )