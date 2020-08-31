from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class CVTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def site_login(self):
        self.browser.get('http://localhost:8000/accounts/login')
        self.browser.find_element_by_id('id_username').send_keys("YOUR_USERNAME")
        self.browser.find_element_by_id('id_password').send_keys("YOUR_PASSWORD")
        self.browser.find_element_by_id('submit').click()
    
    def edit_cv(self, id, text):
        editCV = self.browser.find_element_by_id('edit_cv')
        editCV.click()
        time.sleep(1)
        input_education = self.browser.find_element_by_id(id)
        input_education.send_keys(text)
        self.browser.find_element_by_id('submit').click()
        time.sleep(1)


    def test_admin_can_view_and_edit_cv(self): #NEEDS ADMIN LOGIN + make sure 1 empty cv model exists

        self.site_login()
        time.sleep(1)

        #I take a look at my CV
        self.browser.get('http://localhost:8000/cv')

        #The header and page title have my name
        self.assertIn('Marcos Manning', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Marcos Manning', header_text)

        #I can see my contact details
        contactTitle = self.browser.find_element_by_id('contact_details').text
        self.assertIn('Contact Details', contactTitle)
        #all the details are correct
        contact = self.browser.find_element_by_class_name('contact').text
        self.assertIn('295 Champs Sur Marne\nBradley Stoke\nBristol, BS32 9BZ', contact) #make sure each address line is a new line
        self.assertIn('07865155338', contact)
        self.assertIn('marcosmanning@outlook.com', contact)

        #I take a look at my education history 
        educationTitle = self.browser.find_element_by_id('education_details').text
        self.assertIn('Education', educationTitle)

        #I edit the education history 
        self.edit_cv('id_education', 'University of Birmingham')

        #verify all the updated details are correct
        education = self.browser.find_element_by_class_name('education').text
        self.assertIn('University of Birmingham', education)

        #I take a look through my tech skills
        techTitle = self.browser.find_element_by_id('tech_details').text
        self.assertIn('Tech Skills', techTitle)

        #I edit the tech skills history 
        self.edit_cv('id_tech_skills', 'Python')

        #verify all the updated details are correct
        tech = self.browser.find_element_by_class_name('tech').text
        self.assertIn('Python', tech)

        #I take a look through my work experience
        workTitle = self.browser.find_element_by_id('work').text
        self.assertIn('Work Experience', workTitle)

        #I edit the work experience history
        self.edit_cv('id_work_experience', 'Tesco')
        
        #verify all the details are correct
        work = self.browser.find_element_by_class_name('work_details').text
        self.assertIn('Tesco', work)

        #Finally I check my additional skills
        additionalTitle = self.browser.find_element_by_id('additional').text
        self.assertIn('Additional Skills', additionalTitle)
        
        #I edit the skills
        self.edit_cv('id_additional_skills', 'Portuguese')

        #verify all the details are correct
        additional = self.browser.find_element_by_class_name('additional_skills').text
        self.assertIn('Portuguese', additional)

        #Make sure to remove data after test run


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  