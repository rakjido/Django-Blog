import time

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.contrib.auth.models import User

from board.models import Board


class TestFunctionalBlogList(StaticLiveServerTestCase):
    @classmethod
    def setUp(self):
        # Windows
        self.browser = webdriver.Chrome("test_functional/chromedriver.exe")
        self.user = User.objects.create_user("testuser", "testuser@gmail.com", "1234")

    @classmethod
    def tearDown(self):
        self.browser.close()

    def test_functional_dir_displayed(self):
        # 사용자가 home화면을 요청한다.

        self.browser.get(self.live_server_url)
        # time.sleep(50)
        elem = self.browser.find_element_by_id("login")
        self.assertEquals(elem.text, "Log-in")

    def test_fuctional_redirect_to_login(self):
        # login을 클릭했을 때 login url로 이동하는지 여부
        self.browser.get(self.live_server_url)
        login_url = self.live_server_url + reverse("login")
        self.browser.find_element_by_id("login").click()
        self.assertEquals(self.browser.current_url, login_url)

    def test_functional_login_success(self):
        # login이 성공하는지 여부
        self.browser.get(self.live_server_url + reverse("login"))
        user_id = self.browser.find_element_by_id("id_username")
        user_id.clear()
        user_id.send_keys("testuser")
        passwd = self.browser.find_element_by_id("id_password")
        passwd.clear()
        passwd.send_keys("1234")
        self.browser.find_element_by_class_name("btn").click()
        self.assertEquals(self.browser.current_url, "{}/".format(self.live_server_url))

    # def test_functional_login_fail(self):
    #     pass

    def test_functional_redirect_to_new_post(self):
        # 로그인 되어 있을 때 새로 글쓰기(new) url로 이동하는지 여부
        self.loggin_process()
        self.browser.find_element_by_class_name("btn-primary").click()
        new_url = self.live_server_url + reverse("board_post")
        self.assertEquals(self.browser.current_url, new_url)

    # def test_functional_new_post_sucess(self):
    #     pass

    def test_functional_new_post(self):
        # 글쓰기가 저장되는지 여부
        self.loggin_process()
        self.browser.get(self.live_server_url + reverse("board_post"))
        title = self.browser.find_element_by_id("title")
        title.send_keys("test")
        content = self.browser.find_element_by_id("content")
        content.send_keys("this is test")
        self.browser.find_element_by_id("save").submit()
        self.assertEquals(Board.objects.get(idx=1).title, "test")
        self.assertEquals(self.browser.current_url, "{}/".format(self.live_server_url))

    # def test_functional_new_post_no_data(self):
    #     pass

    # def test_functional_redirect_to_update(self):
    #     pass

    # def test_functional_update_post(self):
    #     pass

    # def test_functional_update_post_no_data(self):
    #     pass

    # def test_functional_redirect_to_delete(self):
    #     pass

    # def test_functional_delete_post(self):
    #     pass

    def loggin_process(self):
        self.browser.get(self.live_server_url + reverse("login"))
        self.browser.find_element_by_id("id_username").send_keys("testuser")
        self.browser.find_element_by_id("id_password").send_keys("1234")
        self.browser.find_element_by_class_name("btn-primary").click()
