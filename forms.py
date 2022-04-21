from wtforms import StringField, IntegerField, SubmitField, validators, TextAreaField, SelectField, FormField , EmailField
from flask_wtf import FlaskForm, Form
from wtforms.validators import DataRequired, Length, Email, ValidationError
import phonenumbers

class SearchBar(FlaskForm):
    search_string = StringField("Search", validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Search')

class Telegram(FlaskForm):
    telegram = StringField(validators=[Length(max=50)])

class PhoneForm(FlaskForm):
    phone = StringField('Phone')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')



class CreateUserForm(FlaskForm):
    something = EmailField('email')
    phone = StringField('phone')
    telegram = StringField('Telegram')


    def validate(self, extra_validators=None):
        if super().validate(extra_validators):
            if not (self.phone.data or self.something.data or self.telegram.data):
                self.something.errors.append('At least one contact')
                return False
            else:
                if self.phone.data:
                    self.something.data += f"./.{self.phone.data}"
                if self.telegram.data:
                    self.something.data += f"./.{self.telegram.data}"

                return True

        return False

class BigForm(FlaskForm):
    title = StringField('Title of item', validators=[DataRequired(), Length(max=30)])
    description = TextAreaField('Describe the item', validators=[DataRequired(), Length(max=120)])
    area_of_service = StringField('Which areas you give service?', validators=[DataRequired(), Length(max=50)])
    wallet_add = StringField('What is the receiving wallet address?', validators=[DataRequired(), Length(max=32)])
    contact_info = FormField(CreateUserForm)
    submit = SubmitField('Submit Item')
