from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=30)
    email = fields.TextField()
    name = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "users"

    def __str__(self):
        return self.username


UserSchema = pydantic_model_creator(User)
UserInSchema = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
