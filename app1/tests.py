from django.test import TestCase
from django.core.urlresolvers import reverse
from django_selenium.livetestcases import SeleniumLiveTestCase
from django_selenium.testcases import SeleniumElement, NoElementException

# Create your tests here.

class MyTestCase(SeleniumLiveTestCase):

    def test_home(self):
        self.driver.open_url(reverse('index_page'))
        #self.open_url(reverse('inner_page'))
        import time
        time.sleep(10)
        self.assertEquals(self.driver.get_title(), 'First page')
        