from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


STATES = (
	('COMPLETED', 'COMPLETED'),
	('WORKING', 'WORKING'),
	('TODO', 'TODO')
)


class TODO(models.Model):
    title =  models.CharField(max_length=500)
    description =  models.TextField()
    state = models.TextField(choices=STATES)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'TODO'
        verbose_name_plural = "TODO's"
    def __str__(self):
        return self.title
