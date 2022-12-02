from django.db import models
# Create your models here.
class Field(models.Model):
    list_select = (
        ('1', 'Hello'),
        ('2', 'World'),
    )
    list_boolean = (
        (True, 'True'),
        (False, 'False'),
    )

    # big_integer_field = models.BigIntegerField(verbose_name="Big Integer Field", help_text="Big integer field", error_messages="Vui lòng nhập lại")
    # boolean_field = models.BooleanField(verbose_name="Boolean Field", help_text="Boolean Field", error_messages="Vui lòng nhập lại")
    # select_muitiple_filed = models.CharField(max_length=100, verbose_name="Select Field", help_text="Select Field")    
    # binary_field = models.BinaryField(verbose_name="Binary Field", help_text="Binary Field", error_messages="Vui lòng nhập lại")
    # char_filed =  models.CharField(editable=True, null=True, max_length=100, verbose_name="Char Field", help_text="Char Field", error_messages="Vui lòng nhập lại" )
    # select_filed =  models.CharField(choices=list_select ,max_length=100, verbose_name="Select Field", help_text="Select Field")
    # date_filed = models.DateField(verbose_name="Date Field", help_text="Date Field", error_messages="Vui lòng nhập lại")
    # dateTime_filed =  models.DateTimeField(verbose_name="DateTime Field", help_text="DateTime Field", error_messages="Vui lòng nhập lại")
    # duration_filed =  models.DurationField(verbose_name="Duration Field", help_text="Duration Field", error_messages="Vui lòng nhập lại")
    # email_filed =  models.EmailField(verbose_name="Email Field", help_text="Email Field", error_messages="Vui lòng nhập lại")
    # float_filed =  models.FloatField(verbose_name="Float Field", help_text="Float Field", error_messages="Vui lòng nhập lại")
    # integer_filed =  models.IntegerField(verbose_name="Integer Field", help_text="Integer Field", error_messages="Vui lòng nhập lại")
    # decimal_filed =  models.DecimalField(decimal_places=3, max_digits=12,verbose_name="Decimal Field", help_text="Decimal Field", error_messages="Vui lòng nhập lại" )
    # image_filed =  models.ImageField(upload_to='',verbose_name="Image Field", help_text="Image Field", error_messages="Vui lòng nhập lại")
    # json_field = models.JSONField(verbose_name="JSON Field", help_text="JSON Field", error_messages="Vui lòng nhập lại")
    # file_filed =  models.FileField(upload_to='',default='',verbose_name="File Field", help_text="File Field", error_messages="Vui lòng nhập lại")  
    # generic_ip_address_filed = models.GenericIPAddressField(verbose_name="Generic IP Address Field", help_text="Generic IP Address Field", error_messages="Vui lòng nhập lại")
    # positive_integer_field = models.PositiveIntegerField(verbose_name="Positive Integer Field", help_text="Positive Integer Field", error_messages="Vui lòng nhập lại")
    # positive_small_integer_field = models.PositiveSmallIntegerField(verbose_name="Positive Field", help_text="Positive Field", error_messages="Vui lòng nhập lại") 
    # slug_filed =  models.SlugField(verbose_name="Slug Field", help_text="Slug Field", error_messages="Vui lòng nhập lại")
    # small_integer_field = models.SmallIntegerField(verbose_name="Small Field", help_text="Small Field", error_messages="Vui lòng nhập lại")
    # time_filed =  models.TimeField(verbose_name="Time Field", help_text="Time Field", error_messages="Vui lòng nhập lại")
    # text_field = models.TextField(verbose_name="Text File", help_text="Text File", error_messages="Vui lòng nhập lại")
    # url_filed =  models.URLField(verbose_name="Url File", help_text="Url File", error_messages="Vui lòng nhập lại")
    uuid_filed =  models.UUIDField(verbose_name="UUID Field", help_text="UUID Field", error_messages="Vui lòng nhập lại")