from django.db import models
from django.contrib.auth.models import User
from book.models import Book
import uuid
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    order_created_at = models.DateTimeField(auto_now_add=True)

    