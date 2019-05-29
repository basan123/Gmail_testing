from helpers.signIn import signIn

class Test_gmail_signin_signout(signIn):

    @classmethod
    def setup_class(cls):
        print('\nclass', cls.__name__)

    @classmethod
    def teardown_class(cls):
        print('\nclass', cls.__name__)

    def setup_method(self):
        self.signinid='basanagowda23@gmail.com'
        self.password='9902188328'
        print('\nMethod')
        self.test=True
        

    def teardown_method(self):
        print('\nMethod')
        self.driver.quit()
        self.test=True

    def test_gmail_signin_signout_testing(self):
        print('\n\n\n\n\n',self.test)
        self.test=False
        print('\n\n\n\n\n',self.test)
        sign=signIn.sign_in(self, self.signinid,self.password)   
        inbox = sign.sign_in()
        print(inbox) 


    def test_2(self):
        print('\n\n\n\n\n',self.test)

# class TestClass:
#     @classmethod
#     def setup_class(cls):
#        print('\nsetUp class', cls.__name__)

#     @classmethod
#     def teardown_class(cls):
#        print('\nteardown class', cls.__name__)

#     def setup_method(self):
#         print('\nsetUP method')

#     def teardown_method(self):
#         print('\ntear down method')


#     def test_tc1(self):
#         print('test1') 

#     def test_tc2(self):
#         print('test2') 