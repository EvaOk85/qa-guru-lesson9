from data import users
from page_objects.model_pages import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    student = users.student
    registration_page.open()
    registration_page.simle_register(student)
    registration_page.should_registered_user(student)