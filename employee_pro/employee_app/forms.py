from django import forms

class Employee_Form(forms.Form):
    empno = forms.IntegerField(
        label='Employee Id:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Employee Id'
            }
        )
    )
    firstname = forms.CharField(
        label='First Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your First Name'
            }
        )
    )
    lastname = forms.CharField(
        label='Last Name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Last Name'
            }
        )
    )
    salary = forms.DecimalField(
        label='Salary:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Salary'
            }
        )
    )
    location = forms.CharField(
        label='Location:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Location'
            }
        )
    )
    company = forms.CharField(
        label='Company:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Company'
            }
        )
    )
    position = forms.CharField(
        label='Position:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Position'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Mobile No:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label='Email Id:',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email Id'
            }
        )
    )

