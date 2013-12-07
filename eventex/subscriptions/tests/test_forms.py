# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        """
        Form must have 4 fields.
        """
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        """
        CPF must only accept digits.
        """
        data = dict(name='Henrique Bastos', email='henrique@bastos.net',
                    cpf='12345678901', phone='21-996186180')
        data.update({'cpf': 'ABCD5678901'})
        form = SubscriptionForm(data)
        form.is_valid()

        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        """
        CPF must have 11 digits.
        """
        data = dict(name='Henrique Bastos', email='henrique@bastos.net',
                    cpf='12345678901', phone='21-996186180')
        data.update({'cpf': '1234'})
        form = SubscriptionForm(data)
        form.is_valid()

        self.assertItemsEqual(['cpf'], form.errors)
