from django.test import TestCase
from blog.models import CV

class CVPageTest(TestCase):

    def test_uses_cv_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv/cv.html')

    def test_cv_shows_all_items(self):
        CV.objects.create(education='University of Birmingham', tech_skills='Python')

        response = self.client.get('/cv')

        self.assertIn('University of Birmingham', response.content.decode())
        self.assertIn('Python', response.content.decode())

class CvModelTest(TestCase):

    def test_adding_and_retrieving(self):
        cv = CV()
        cv.education = 'University of Birmingham'
        cv.tech_skills = 'Python'
        cv.save()

        saved_cv = CV.objects.all()
        self.assertEqual(saved_cv.count(), 1)
        
        complete_cv = saved_cv[0]

        self.assertEqual(complete_cv.education, 'University of Birmingham')
        self.assertEqual(complete_cv.tech_skilss, 'Python')


