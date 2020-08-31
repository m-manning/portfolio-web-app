from django.test import TestCase
from blog.models import CV

class CVPageTest(TestCase):

    def test_uses_cv_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv/cv.html')

    def test_cv_shows_all_items(self):
        CV.objects.create(education='University of Birmingham', tech_skills='Python', 
        work_experience='Tesco', additional_skills='Portuguese')

        response = self.client.get('/cv')

        self.assertIn('University of Birmingham', response.content.decode())
        self.assertIn('Python', response.content.decode())
        self.assertIn('Tesco', response.content.decode())
        self.assertIn('Portuguese', response.content.decode())

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv')
        self.assertEqual(CV.objects.count(), 0)

class CvModelTest(TestCase):

    def test_adding_and_retrieving(self):
        cv = CV()
        cv.education = 'University of Birmingham'
        cv.tech_skills = 'Python'
        cv.work_experience = 'Tesco'
        cv.additional_skills = 'Portuguese'
        cv.save()

        saved_cv = CV.objects.all()
        self.assertEqual(saved_cv.count(), 1)
        
        complete_cv = saved_cv[0]

        self.assertEqual(complete_cv.education, 'University of Birmingham')
        self.assertEqual(complete_cv.tech_skills, 'Python')
        self.assertEqual(cv.work_experience, 'Tesco')
        self.assertEqual(cv.additional_skills, 'Portuguese')


