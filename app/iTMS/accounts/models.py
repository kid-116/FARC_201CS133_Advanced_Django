from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from sections.models import Section

class AccountManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None, is_staff=False, is_admin=False, is_active=True):
        if not username:
            raise ValueError("Username must be entered!")
        if not password:
            raise ValueError("Password must be entered!")
        user_obj = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
    def create_staffuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(
            username,
            email,
            first_name,
            last_name,
            password=password,
            is_staff=True
        )
        return user
    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(
            username,
            email,
            first_name,
            last_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    section = models.ForeignKey(Section, blank=True, null= True, on_delete=models.DO_NOTHING, related_name='students')
    is_cr = models.BooleanField(default=False, verbose_name="Is CR")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
    ]
    objects = AccountManager()
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True