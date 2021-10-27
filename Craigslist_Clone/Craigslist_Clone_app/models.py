from django.db import models

# Create your models here.


class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # We don't want to see the newly added object as Search object 1, Rather we want the search itself as the name
    def __str__(self):
        return '{}'.format(self.search)

    # We don't want to see Searchs as it is wrong so changing the plural to Searches
    class Meta:
        verbose_name_plural = 'Searches'
