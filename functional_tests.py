from selenium import webdriver
import unittest

class CVTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_view_cv(self):  

        #An employer checks out Marcos' CV
        self.browser.get('http://localhost:8000/cv')

        #They notice the header and page title have his name
        self.assertIn('Marcos Manning', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Marcos Manning', header_text)

        #They notice his contact details 
        contactTitle = self.browser.find_element_by_id('contact_details').text
        self.assertIn('Contact Details', contactTitle)
        #all the details are correct
        contact = self.browser.find_element_by_class_name('contact').text
        self.assertIn('295 Champs Sur Marne\nBradley Stoke\nBristol, BS32 9BZ', contact) #make sure each address line is a new line
        self.assertIn('07865155338', contact)
        self.assertIn('marcosmanning@outlook.com', contact)

        #They take a look at his education history 
        self.fail('Finish the test!')  

        #They then take a look at his tech skills

        #They then look through his work experience

        #Finally they can see his additional skills 


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  