import json
import allure
from allure import attachment_type


def test_attachments():
    allure.attach('Test', name='Text', attachment_type=attachment_type.TEXT)
    allure.attach('<h1>Test</h1>', name='Html', attachment_type=attachment_type.HTML)
    allure.attach(json.dumps('Test'), name='Json', attachment_type=attachment_type.JSON)
