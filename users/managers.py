from django.contrib.auth.base_user import BaseUserManager


class CustomUserManger(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        user = self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        user = self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        user.is_admin = True
        user.is_superuser = True

        if user.is_superuser is not True:
            raise ValueError('Superuser must have assign to is_superuser=True.')
        if user.is_active is not True:
            raise ValueError('Superuser must have assign to is_active=True.')
        user.save()
        return user
