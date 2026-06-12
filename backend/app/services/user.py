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

    def __str__(
        self
    ):

        return (
            f"User("
            f"username={self.username}, "
            f"role={self.role}"
            f")"
        )