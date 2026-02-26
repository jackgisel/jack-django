from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model. Extend with additional fields as needed."""

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
