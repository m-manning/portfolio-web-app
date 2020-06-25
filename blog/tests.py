from django.test import TestCase

class CVPageTest(TestCase):

    def test_uses_cv_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'cv/cv.html')
