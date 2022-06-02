from django_countries.widgets import CountrySelectWidget
from django import forms
from django.forms import Form
from .models import Person
import datetime
from material import Row, Layout, Fieldset
from material import *



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['country']
        widgets = {
            'country': CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'}),
        }





class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
    receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Personal details',
                             Row('first_name', 'last_name'),
                             'gender', 'receive_news', 'agree_toc'))

    title = "Registration form"



COUNTRY_CHOICES = (
    'Ghana', 'Ghana',
    'Nigeria', 'Nigeria',
    'Algeria', 'Algeria',
)

class BankForm(forms.Form):
    branch_name = forms.CharField()

    """ Personal Details """
    person_title = forms.ChoiceField(choices=(('Mr', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')), label='Title')
    full_name = forms.CharField()
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    parent_name = forms.CharField(label='In case of a minor please provide details')
    nationality = forms.ChoiceField(choices=COUNTRY_CHOICES)
    mobile_no = forms.CharField()
    existing_bank_account = forms.CharField()
    partner_name = forms.CharField(label='Name of father/spouse')

    """ Residential address """
    flat_bulding = forms.CharField(label='Flat no. and bldg. name')
    road_no = forms.CharField(label='Road no./name')
    area_and_landmark = forms.CharField(label='Area and landmark')
    telephone_residence = forms.CharField()
    city = forms.CharField()
    office = forms.CharField()
    fax = forms.CharField()
    pin_code = forms.CharField()

    """ Mailing Address """
    mailing_company_details = forms.CharField(label="Company name and department/ Flat no. and bldg. name")
    mailing_road_no = forms.CharField(label='Road no./name')
    mailing_area_and_landmark = forms.CharField(label='Area and landmark')
    mailing_city = forms.CharField(label='City')
    mailing_mobile = forms.CharField(label='Mobile No.')
    mailing_telephone_residence = forms.CharField(label='Telephone Residence')
    mailing_office = forms.CharField(label='Office')
    mailing_fax = forms.CharField(label='Fax')
    mailing_pin_code = forms.CharField(label='Pin Code')
    mailing_email = forms.EmailField(label='E-mail')

    """ Details of Introduction by Existing Customer """
    introducer_name = forms.CharField(label='Customer Name')
    introducer_account_no = forms.CharField(label='Account No.')
    introducer_signature = forms.CharField(label="Introducer's signature")

    """ Account Details """
    account_type = forms.ChoiceField(
        choices=(('S', 'Savings'), ('C', 'Current'), ('F', 'Fixed deposits')),
        label='Choice of account',
        widget=forms.RadioSelect)
    account_mode = forms.ChoiceField(
        choices=(('CS', 'Cash'), ('CQ', 'Cheque'), ('NF', 'NEFT')),
        label='Mode of funding',
        widget=forms.RadioSelect)
    account_amount = forms.FloatField(label='Amount')

    """ Details of Fixed Deposit """
    deposit_type = forms.ChoiceField(
        choices=(('O', 'Ordinary'), ('C', 'Cumulative')),
        label='Types of deposit',
        widget=forms.RadioSelect)
    deposit_mode = forms.ChoiceField(
        choices=(('CS', 'Cash'), ('CQ', 'Cheque'), ('NF', 'NEFT')),
        label='Mode of funding',
        widget=forms.RadioSelect)
    deposit_amount = forms.FloatField(label='Amount')
    deposit_no = forms.CharField(label='No. of deposits')
    deposit_individual_amount = forms.FloatField(label='Individual Deposit Amount')

    """ Personal Details """
    occupation = forms.ChoiceField(
        choices=(('NE', 'Non-executive'), ('HW', 'Housewife'), ('RT', 'Retired'),
                 ('ST', 'Student'), ('OT', 'Other'), ('UN', 'Unemployed')),
        widget=forms.RadioSelect)
    job_title = forms.CharField()
    department = forms.CharField()
    nature_of_business = forms.CharField()
    education = forms.ChoiceField(
        choices=(('UG', 'Under graduate'), ('GR', 'Graduate'), ('OT', 'Others')),
        widget=forms.RadioSelect)
    montly_income = forms.ChoiceField(
        choices=(('000', 'Zero Income'), ('L10', 'Less than $10,000'), ('G10', '$10,000+')),
        widget=forms.RadioSelect)
    martial_status = forms.ChoiceField(
        choices=(('M', 'Married'), ('S', 'Single')),
        widget=forms.RadioSelect)
    spouse_name = forms.CharField()

    """ Other existing bank accounts, if any """
    other_account1 = forms.CharField(label='Name of the Bank / branch')
    other_account2 = forms.CharField(label='Name of the Bank / branch')

    """ Reason for Account opening """
    reason = forms.CharField(label="Please specify", widget=forms.Textarea)

    """ Terms And Conditions """
    terms_accepted = forms.BooleanField(
        label="I/We confirm having read and understood the account rules of The Banking Corporation Limited"
        " ('the Bank'), and hereby agree to be bound by the terms and conditions and amendments governing the"
        " account(s) issued by the Bank from time-to-time.")

    layout = Layout(
        Fieldset("Please open an account at",
                 'branch_name'),
        Fieldset("Personal Details (Sole/First Accountholder/Minor)",
                 Row(Span2('person_title'), Span10('full_name')),
                 Row(Column('date_of_birth',
                            'email',
                            'parent_name'),
                     Column('nationality',
                            Row('mobile_no', 'existing_bank_account'),
                            'partner_name'))),
        Fieldset('Residential address',
                 Row('flat_bulding', 'road_no'),
                 Row(Span10('area_and_landmark'), Span2('city')),
                 Row('telephone_residence', 'office', 'fax', 'pin_code')),
        Fieldset("Mailing Address (If different from the First Accountholder's address)",
                 'mailing_company_details',
                 Row('mailing_road_no', 'mailing_area_and_landmark', 'mailing_city', 'mailing_mobile'),
                 Row('mailing_telephone_residence', 'mailing_office', 'mailing_fax', 'mailing_pin_code'),
                 'mailing_email'),
        Fieldset("Details of Introduction by Existing Customer (If applicable)",
                 Row('introducer_name', 'introducer_account_no'),
                 'introducer_signature'),
        Fieldset("Account Details",
                 Row('account_type', 'account_mode'),
                 'account_amount'),
        Fieldset("Details of Fixed Deposit",
                 Row('deposit_type', 'deposit_mode'),
                 Row(Span6('deposit_amount'), Span3('deposit_no'), Span3('deposit_individual_amount'))),
        Fieldset("Personal Details",
                 Row('occupation', 'education', 'montly_income'),
                 'job_title',
                 Row('department', 'nature_of_business'),
                 Row('martial_status', 'spouse_name')),
        Fieldset("Other existing bank accounts, if any",
                 Row('other_account1', 'other_account2')),
        Fieldset("Reason for Account opening",
                 'reason'),
        Fieldset("Terms And Conditions",
                 'terms_accepted')
    )



QUESTION_CHOICES = (
    ('I have a history of problems with anesthesia', 'I have a history of problems with anesthesia'),
    ('I have been addicted to recreational drugs', 'I have been addicted to recreational drugs'),
    ('I weak  eye contact lenses or glasses', 'I weak  eye contact lenses or glasses'),
    ('I have an implantable devise', 'I have an implantable devise'),
    ('Blood has been donated for this procedure by a family member', 'Blood has been donated for this procedure by a family member'),
    ('I consume alcohol on a regular basis', 'I consume alcohol on a regular basis'),
    ('I have teeth and mouth considerations such as loose teeth, caps, bridework, banding, and dentures'),
    ('I have a vascular access devise', 'I have a vascular access devise'),

    )


CARDIOVASCULAR_RISK_CHOICES = (
    ('Heart Attack', 'Heart Attack'),
    ('Angina', 'Angina'),
    ('Coronary Artery Disease', 'Coronary Artery Disease'),
    ('Stroke', 'Stroke'),
    ('Coronary Artery Bypass Graft', 'Coronary Artery Bypass Graft'),
    ('Valvular Heart Disease', 'Valvular Heart Disease'),
    ('Heart Failure', 'Heart Failure'),
    ('Heart Bypass Surgery', 'Heart Bypass Surgery'),
    ('Heart Transplant', 'Heart Transplant'),
    ('High Blood Pressure', 'High Blood Pressure'),

    )


APNIA_RISK_CHOICES = (
    ('Loud Snoring', 'Loud Snoring'),
    ('Sleep Apnea', 'Sleep Apnea'),
    ('Choking while asleep', 'Choking while asleep'),
    ('Emphysema', 'Emphysema'),
    ('Pheumonia', 'Pheumonia'),
    ('Asthma', 'Asthma'),
    ('Bronchitis', 'Bronchitis'),
    ('Bleeding Disorder', 'Bleeding Disorder'),
    ('Aids or HIV', 'Aids or HIV'),
    ('Cancer', 'Cancer'),
    ('Diabetes', 'Diabetes'),
    ('High Cholesterol', 'High Cholesterol'),
    ('High Blood Pressure', 'High Blood Pressure'),
    ('High Blood Sugar', 'High Blood Sugar'),
    ('Bruise Easy', 'Bruise Easy'),
    ('Bruise Hard', 'Bruise Hard'),
    ('Bruise Painful', 'Bruise Painful'),
    ('Bruise Painless', 'Bruise Painless'),
    ('Kidney Problems', 'Kidney Problems'),
    ('Liver Problems', 'Liver Problems'),
    ('Lung Problems', 'Lung Problems'),
    ('Muscle Problems', 'Muscle Problems'),
    ('Nose Problems', 'Nose Problems'),
    ('Stomach Problems', 'Stomach Problems'),
    ('Tooth Problems', 'Tooth Problems'),
    ('Tonsillitis', 'Tonsillitis'),
    ('Urinary Tract Infection', 'Urinary Tract Infection'),
    ('Viral Infection', 'Viral Infection'),
    ('Warts', 'Warts'),
    ('Wound Infection', 'Wound Infection'),

    )


# class HospitalRegistrationForm(Form, forms.Form):
#     class EmergencyContractForm(forms.Form):
#         name = forms.CharField()
#         relationship = forms.ChoiceField(choices=(
#             ('SPS', 'Spouse'), ('PRT', 'Partner'),
#             ('FRD', 'Friend'), ('CLG', 'Colleague')))
#         daytime_phone = forms.CharField()
#         evening_phone = forms.CharField(required=False)

#     EmergencyContractFormSet = forms.formset_factory(
#         EmergencyContractForm, extra=1, can_delete=True)


#     registration_date = forms.DateField(initial=datetime.date.today)
#     full_name = forms.CharField()
#     birth_date = forms.DateField()
#     height = forms.IntegerField(help_text='cm')
#     weight = forms.IntegerField(help_text='kg')
#     primary_care_physician = forms.CharField()
#     date_of_last_appointment = forms.DateField()
#     home_phone = forms.CharField()
#     work_phone = forms.CharField(required=False)

#     procedural_questions = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple, required=False,
#         choices=QUESTION_CHOICES)

#     cardiovascular_risks = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple, required=False,
#         choices=CARDIOVASCULAR_RISK_CHOICES)

#     apnia_risks = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple, required=False,
#         choices=APNIA_RISK_CHOICES)

#     # emergency_contacts = FormSetField(EmergencyContractFormSet) # pro only

#     layout = Layout(Row(Column('full_name', 'birth_date',
#                                Row('height', 'weight'), span_columns=3), 'registration_date'),
#                     Row(Span3('primary_care_physician'), 'date_of_last_appointment'),
#                     Row('home_phone', 'work_phone'),
#                     Fieldset('Procedural Questions', 'procedural_questions'),
#                     Fieldset('Clinical Predictores of Cardiovascular Risk', 'cardiovascular_risks'),
#                     Fieldset('Clinical Predictors of sleep Apnia Risk', 'apnia_risks'),
#                     Fieldset('Emergency Contacts', 'emergency_contacts'))