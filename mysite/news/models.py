from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Sarlavha')
    content = models.TextField(null=True, blank=True, verbose_name='Maqola')
    create = models.DateTimeField(auto_now_add=True, db_index=True)
    update = models.DateTimeField(auto_now=True, db_index=True)
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-update']

    def __str__(self):
        return self.title