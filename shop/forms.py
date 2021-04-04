from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from .import models
from datetime import date


User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    
    class Meta():
        model = models.Customer
        fields = ('first_name', 'last_name','gender', 'location', 'phone')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name...'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location...'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Mobile Number...'}),
        }
        
        labels ={
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'location': 'Location',
            'phone': 'Mobile No.'
        }
    

class FemaleMeasurementForm(forms.ModelForm):

    class Meta():
        model = models.Customer
        fields = ('accross_back', 'around_arm', 'bust',
                  'hips', 'waist', 'dress_lenght', 'shoulder_to_under_bust',
                   'shoulder_to_waist','top_or_shirt_length', 'skirt_or_trouser_length')

        widgets = {
            'accross_back': forms.TextInput(attrs={'placeholder': 'Accross Back...'}),
            'around_arm': forms.TextInput(attrs={'placeholder': 'Around Arm...'}),
            'bust': forms.TextInput(attrs={'placeholder': 'Bust...'}),
            'hips': forms.TextInput(attrs={'placeholder': 'Hips...'}),
            'waist': forms.TextInput(attrs={'placeholder': 'Waist...'}),
            'dress_lenght': forms.TextInput(attrs={'placeholder': 'Dress Lenght...'}),
            'shoulder_to_under_bust': forms.TextInput(attrs={'placeholder': 'Shoulder To Under Bust...'}),
            'shoulder_to_waist': forms.TextInput(attrs={'placeholder': 'Shoulder To Waist...'}),
            'top_or_shirt_length': forms.TextInput(attrs={'placeholder': 'Top Lenght...'}),
            'skirt_or_trouser_length': forms.TextInput(attrs={'placeholder': 'Skirt Lenght...'}),
        }

        labels = {
            'dress_lenght': 'Dress Lenght',
            'shoulder_to_under_bust': 'Shoulder To Under Bust',
            'shoulder_to_waist': 'Shoulder To Waist',
            'top_or_shirt_length': 'Top Length',
            'skirt_or_trouser_length': 'Skirt Length',
            
        }


class MaleMeasurementForm(forms.ModelForm):
    
    class Meta():
        model = models.Customer
        fields = ('accross_back', 'around_arm',
                  'hips', 'waist', 'top_or_shirt_length', 'skirt_or_trouser_length',
                  'chest', 'sleeves', 'thigh','bar'
                  
                   )

        widgets = {
            'accross_back': forms.TextInput(attrs={'placeholder': 'Accross Back...'}),
            'around_arm': forms.TextInput(attrs={'placeholder': 'Around Arm...'}),
            'hips': forms.TextInput(attrs={'placeholder': 'Hips...'}),
            'waist': forms.TextInput(attrs={'placeholder': 'Waist...'}),
            'top_or_shirt_length': forms.TextInput(attrs={'placeholder': 'Shirt Lenght...'}),
            'skirt_or_trouser_length': forms.TextInput(attrs={'placeholder': 'Trouser Lenght...'}),
            'chest': forms.TextInput(attrs={'placeholder': 'Chest...'}),
            'sleeves': forms.TextInput(attrs={'placeholder': 'Sleeves...'}),
            'thigh': forms.TextInput(attrs={'placeholder': 'Thigh...'}),
        }

        labels = {
            'top_or_shirt_length': 'Shirt Length',
            'skirt_or_trouser_length': 'Trouser Length',          
        }


class OrderForm(forms.ModelForm):

    class Meta():
        model = models.Order
        fields = ('price', 'amount_paid', 'balance','closing_date')
    
        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'price...'}),
            'amount_paid': forms.TextInput(attrs={'placeholder': 'Amount Paid...'}),
            'balance': forms.TextInput(attrs={'placeholder': 'Balance...'}),
            'closing_date': DateInput(),
        }

class EditOrderForm(forms.ModelForm):
    
    class Meta():
        model = models.Order
        fields = ('price', 'amount_paid', 'balance','status','closing_date')

        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'price...'}),
            'amount_paid': forms.TextInput(attrs={'placeholder': 'Amount Paid...'}),
            'balance': forms.TextInput(attrs={'placeholder': 'Balance...'}),
            'closing_date': DateInput(),
        }


class ExpenditureForm(forms.ModelForm):

    class Meta():
        model = models.Expenditure
        fields = ('account_code', 'amount')

        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'Amount ...'}),
        }
        
        labels = {
            'account_code': 'Accounts Code',
            'amount': 'Amount',
        }


class RevenueForm(forms.ModelForm):
    
    class Meta():
        model = models.Revenue
        fields = ('account_code', 'amount')

        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'Amount ...'}),
        }
        
        labels = {
            'account_code': 'Accounts Code  (Orders is not acceptable)',
            'amount': 'Amount',
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password incorrect')
            if not user.check_password(password):
                raise forms.ValidationError('Username or Password incorrect')
            if not user.is_active:
                raise forms.ValidationError('Username or Password incorrect')
        return super(UserLoginForm, self).clean(*args, **kwargs)

    class Meta():
        model = models.User
        fields = ('username', 'password')


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Comfirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

