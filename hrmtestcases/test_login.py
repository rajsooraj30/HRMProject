import pytest
import conftest
from conftest import BaseUrl
from hrmpages.login_page import Login_page

@pytest.mark.usefixtures("browser_setup")
class Test_login:
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page=Login_page(self.driver)

    def test_valid_login(self):
        self.login_page.login(conftest.user_name,conftest.password)

    def teardown_class(self):
        self.driver.quit()