import re

from trekkpay.exceptions import ValidationError
from trekkpay.utils import country_codes


class Model:
    def validate_common_string(self, value):
        self.check_is_empty(value)
        return value

    def validate_instance(self, value, class_object):
        self.check_object_instance(value, class_object)
        return value

    @staticmethod
    def check_is_empty(value):
        if not value.strip():
            raise ValidationError("This field is required. Don't fill the field with whitespaces.")

    @staticmethod
    def check_object_instance(value, class_object):
        if not isinstance(value, class_object):
            raise ValidationError("This object is not a {} instance.".format(class_object.__class__.__name__))


class Account(Model):
    def __init__(self, number, **kwargs):
        """
        Account information.

        :param str number: Bank account number or IBAN.
        :param kwargs: Optional parameters.
        """
        self.number = self.validate_common_string(number)


class BankAbstract(Model):
    def __init__(self, name, address1, postcode, city, country, **kwargs):
        """
        Bank abstract model.

        :param str name: Holder name.
        :param str address1: First address line.
        :param str postcode: ZIP Code.
        :param str city: City / Municipality.
        :param str country: Country code ISO 3166-1 alpha-2.
        """
        self.name = self.validate_common_string(name)
        self.address1 = self.validate_common_string(address1)
        self.postcode = self.validate_common_string(postcode)
        self.city = self.validate_common_string(city)
        self.county = self.validate_country(country)

    @staticmethod
    def validate_country(country):
        if country not in country_codes:
            raise ValidationError("{} is invalid country code.".format(country))
        return country


class Bank(BankAbstract):
    def __init__(self, name, address1, postcode, city, country, swift, **kwargs):
        """
        Bank information.

        :param str name: Holder name.
        :param str address1: First address line.
        :param str postcode: ZIP Code.
        :param str city: City / Municipality.
        :param str country: Country code ISO 3166-1 alpha-2.
        :param str swift: SWIFT / BIC code
        """
        super().__init__(name, address1, postcode, city, country, **kwargs)
        self.swift = self.validate_swift(swift)

    @staticmethod
    def validate_swift(swift):
        rule = re.compile(r'^[A-Z0-9]{8,11}$')
        if not rule.search(swift):
            raise ValidationError("The swift is invalid.")
        return swift


class Holder(BankAbstract):
    """
    Account holder information.
    """


class BankAccount(Model):
    def __init__(self, currency, account, holder, bank, **kwargs):
        """
        A bank account.

        :param str currency: Currency of the bank account.
        :param Account account: Account information.
        :param Holder holder: Account holder information.
        :param Bank bank: Bank information.
        :param kwargs: Optional parameters.
        """
        self.currency = self.validate_common_string(currency)
        self.account = self.validate_instance(account, Account)
        self.holder = self.validate_instance(holder, Holder)
        self.bank = self.validate_instance(bank, Bank)


class Contact(Model):
    def __init__(self, name, email, phone=None, websites=None):
        """
        Merchant contact information.

        :param str name: Name of the contact.
        :param str email: Email address of the contact.
        :param str phone: Phone numbers of the contact.
        :param list websites: Merchant website URLs.
        """
        self.name = self.validate_common_string(name)
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.websites = self.validate_websites(websites)

    @staticmethod
    def validate_email(email):
        if not '@' in email or ' ' in email:
            raise ValidationError("The email address is invalid.")
        return email

    @staticmethod
    def validate_phone(phone):
        rule = re.compile(r'^\+\d{3,}$')
        if not rule.search(phone):
            raise ValidationError("The phone is invalid.")
        return phone

    @staticmethod
    def validate_websites(websites):
        websites = list(filter(len, map(lambda w: w.strip(), websites)))
        return websites
