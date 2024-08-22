from django.db import models
from django.utils.translation import gettext_lazy as _  

class Category(models.Model):
   parent=models.ForeignKey('self', verbose_name=_('parent'), null=True, blank=True, on_delete=models.CASCADE)
   title=models.CharField(_('title'), max_length=50)
   description=models.TextField(_('description'), null=True, blank=True)
   avatar=models.ImageField(_('avatar'), blank=True, upload_to='categories/')
   is_enable=models.BooleanField(_('is enable'), default=True)
   time_create=models.DateTimeField(_('time create'), auto_now_add=True)
   time_update=models.DateTimeField(_('time update'), auto_now=True)
   class Meta:
      db_table='categories'
      verbose_name=_('Category')
      verbose_name_plural=('Categories')

   def __str__(self):
      return self.title



class Product(models.Model):
   title=models.CharField(_('title'), max_length=50)
   description=models.TextField(_('description'), null=True, blank=True)
   avatar=models.ImageField(_('avatar'), blank=True, upload_to='products/')
   categories=models.ManyToManyField('Category', verbose_name=_('category'), blank=True)
   is_enable=models.BooleanField(_('is enable'), default=True)
   time_create=models.DateTimeField(_('time create'), auto_now_add=True)
   time_update=models.DateTimeField(_('time update'), auto_now=True)

   class Meta:
      db_table='products'
      verbose_name=_('Product')
      verbose_name_plural=('Products')
 

   def __str__(self):
      return self.title

class File(models.Model):
   product=models.ForeignKey('Product', verbose_name=_('product'), null=True, blank=True, on_delete=models.CASCADE)
   title=models.CharField(_('title'), max_length=50)
   description=models.TextField(_('description'), null=True, blank=True)
   file=models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
   is_enable=models.BooleanField(_('is enable'), default=True)
   time_create=models.DateTimeField(_('time create'), auto_now_add=True)
   time_update=models.DateTimeField(_('time update'), auto_now=True)
   class Meta:
      db_table='files'
      verbose_name=_('File')
      verbose_name_plural=('Files')

   def __str__(self):
      return self.title