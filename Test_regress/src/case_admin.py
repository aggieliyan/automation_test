
import unittest

class TestAdmin(unittest.TestCase):


    def create_admin(cfg, driver, admin_name, admin_username, admin_psw, admin_email):

        adpage = OrgAdminListPage(driver, cfg)
        adpage.open()
        adpage.click_create()

        editpage = OrgAdminInputPage(driver, cfg)
        editpage.input_name(admin_name)
        editpage.input_username(admin_username)
        editpage.input_password(admin_psw)
        editpage.input_psd_again(admin_psw)
        editpage.input_email(admin_email)
        editpage.input_eml_again(admin_email)
        editpage.click_add_save()
        time.sleep(1)

    def test_create_admin():