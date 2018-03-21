import pytest


@pytest.mark.usefixtures('driver')
class TestLink:

    def test_link(self, driver):
        """
        Verify page title change when link clicked
        :return: None
        """
        driver.get('https://saucelabs-sample-test-frameworks.github.io/training-test-page')
        driver.find_element_by_id("i_am_a_link").click()

        title = "I am another page title - Sauce Labs"
        assert title == driver.title


    def test_comment(self, driver):
        """
        Verify comment submission
        :return: None
        """
        driver.get('https://saucelabs-sample-test-frameworks.github.io/training-test-page')
        sample_text = "hede@hodo.com"
        email_text_field = driver.find_element_by_id("comments")
        email_text_field.send_keys(sample_text)

        driver.find_element_by_id("submit").click()

        text = driver.find_element_by_id("your_comments").text
        assert sample_text in text
