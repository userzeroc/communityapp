from urllib import request
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = {'title', 'url', 'description'}
        widgets = {
            'url': forms.HiddenInput,
        }

        # 判断链接是否有效

    # 清除不符合规则的url
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('此链接不符合图片要求')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),
                                    image_url.split('.', 1)[1].lower())
        # 从给定的url下载图片
        response = request.urlopen(image_url)
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)
        if commit:
            image.save()
        return image
