import pytest
from os import environ

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.remote_connection import RemoteConnection


@pytest.fixture(scope='class')
def driver(request):
    # if the assignment below does not make sense to you please read up on object assignments.
    # The point is to make a copy and not mess with the original test spec.
    desired_caps = {}
    
    browser = {
        "platform": "Windows 10",
        "browserName": "firefox",
        "version": "49.0"
    }

    desired_caps.update(browser)
    test_name = request.node.name
    build_tag = environ.get('BUILD_TAG', None)
    tunnel_id = environ.get('TUNNEL_IDENTIFIER', None)
    username = environ.get('SAUCE_USER', None)
    access_key = environ.get('SAUCE_KEY', None)

    selenium_endpoint = "https://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key)
    desired_caps['build'] = build_tag
    # we can move this to the config load or not, also messing with this on a test to test basis is possible :)
    desired_caps['tunnelIdentifier'] = tunnel_id
    desired_caps['name'] = test_name

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    request.cls.browser = webdriver.Firefox()
    # browser = webdriver.Remote(
    #     command_executor=executor,
    #     desired_capabilities=desired_caps
    # )

    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    # creates one file per test non ideal but xdist is awful
    # if browser:
    #     with open("{}.testlog".format(browser.session_id), 'w') as f:
    #         f.write("SauceOnDemandSessionID=%s job-name=%s\n" % (browser.session_id, test_name))
    # else:
    #     raise WebDriverException("Never created!")

@pytest.fixture(scope='class')
def stop(request):
    def fin():
        #request.cls.browser.execute_script("sauce:job-result={}".format(str(not request.node.rep_call.failed).lower()))
        request.cls.browser.quit()
    request.addfinalizer(fin)


@pytest.mark.usefixtures('driver', 'stop')
class TestLink:

    def test_link(self):
        """
        Verify page title change when link clicked
        :return: None
        """
        self.browser.get('https://saucelabs-sample-test-frameworks.github.io/training-test-page')
        self.browser.find_element_by_id("i_am_a_link").click()

        title = "I am another page title - Sauce Labs"
        assert title == self.browser.title

@pytest.mark.usefixtures('driver', 'stop')
class TestComment:
    def test_comment(self):
        """
        Verify comment submission
        :return: None
        """
        self.browser.get('https://saucelabs-sample-test-frameworks.github.io/training-test-page')
        sample_text = "hede@hodo.com"
        email_text_field = self.browser.find_element_by_id("comments")
        email_text_field.send_keys(sample_text)

        self.browser.find_element_by_id("submit").click()

        text = self.browser.find_element_by_id("your_comments").text
        assert sample_text in text
