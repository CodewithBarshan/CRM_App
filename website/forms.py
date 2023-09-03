from typing import Any, Dict, Mapping, Optional, Type, Union
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Record
# Create your views here.

class SignupForm(UserCreationForm):
    email=forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args,**kwargs):
        super(SignupForm,self).__init__(*args,*kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label='' #this will hide the label name(User name in this case) created by USer model Django automatically 
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required.150 Characters or fewer.Letter,digits and @/./+/-/_ only .</small></span>'
        
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text="<ul class='form-text text-muted small'><li>Your password cant be too similar to other information.</li><li>Your password must contain atleast 8 characters .</li><li>Your password cant be entirely numeric.</li></ul>"

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text="<ul class='form-text text-muted small'><li>Your password must be same as entered in previous field.</li></ul>"
        
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''

class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(max_length=100,required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name","class":"form-control"}),label='')
    last_name=forms.CharField(max_length=100,required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name","class":"form-control"}),label='')
    email=forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}),label='')
    contact_no=forms.CharField(max_length=15,required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Contact No","class":"form-control"}),label='')
    address=forms.CharField(max_length=100,required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}),label='')

    class Meta:
        model=Record
        #exclude=("user",) #this will add all the fieldsNone = ..., auto_id: bool | str = ..., prefix: str | None = ..., initial: Dict[str, Any] | None = ..., error_class: type[ErrorList] = ..., label_suffix: str | None = ..., empty_permitted: bool = .    
        fields=('first_name','last_name','email','contact_no','address')
