from selenium import webdriver
import os
import time

class InstagramBot:
    def __init__(self,username,password):

        '''
        Initializes an instance of the InstagramBot
        call login method


        Args:
           username:str:username of instagram
           password:str:password of instagram

         Attibute:
            driver :slenium webdriver chromedriver that is used to automation

        '''
        self.username=username
        self.password=password
        self.baseurl='https://www.instagram.com'
        self.driver=webdriver.Chrome('./chromedriver.exe')
        self.login()


    def login(self):
        self.driver.get("{}/accounts/login/".format(self.baseurl))
        time.sleep(6)
        self.driver.find_element_by_name('username').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()


    def nav_user(self,user):
        self.driver.get("{}/{}/".format(self.baseurl,user))

    def follow_user(self,user):
        time.sleep(3)
        self.nav_user(user)
        time.sleep(5)
        print('hi')
        follow_button=self.driver.find_element_by_xpath('//button[contains(text(),"Follow")]')
        follow_button.click()
        print(follow_button)

    def unfollow_user(self,user):
        time.sleep(3)
        self.nav_user(user)
        time.sleep(5)
        print('hi')
        unfollow_button=self.driver.find_element_by_xpath('//button[contains(text(),"Following")]')
        unfollow_button.click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//button[contains(text(),"Unfollow")]').click()
        print(unfollow_button)

#react-root > section > main > div > header > section > div.nZSzR > div > button > span
    def auto_log(self,user):
        time.sleep(5)
        self.nav_user(user)
        main_page = self.driver.current_window_handle
        time.sleep(5)
        logout=self.driver.find_elements_by_xpath('/html/body/span/section/main/div/header/section/div[1]/div/button/span')
        print(logout)
        logout[0].click()
        time.sleep(5)



        for handle in self.driver.window_handles:
            if handle != main_page:
                 login_page = handle
        # if login_page==[]:
        #      self.driver.switch_to.window(login_page)
        self.driver.find_element_by_xpath('//button[contains(text(),"Log Out")]').click()

        #
        # logOut=self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div/button[7]')
        # logOut[].click()
        self.driver.switch_to.window(main_page)


if __name__=='__main__':
    ig_bot=InstagramBot('type your username','type your password')
    print(ig_bot.username)
    ig_bot.follow_user('tonyrobbins')
    time.sleep(5)
    ig_bot.unfollow_user('tonyrobbins')
    
    ig_bot.auto_log('type your username')
