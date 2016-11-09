from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(blank=True, default='')
    tags = models.CharField(max_length=300, blank=True,\
        default="")

    def __unicode__(self):
        return self.title

    __str__ = __unicode__

    def get_absolute_url(self):
        return reverse('single_blog', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == '':
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
