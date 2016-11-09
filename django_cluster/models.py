from django.db import models


class DjangoCluster(models.Model):
    blog_json = models.TextField(blank=True, default='')

    @classmethod
    def create(cls, blog_json):
        blog = cls(blog_json=blog_json)
        return blog
