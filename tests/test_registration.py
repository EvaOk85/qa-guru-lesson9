from page_objects.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()


    # WHEN
    registration_page.fill_first_name('Olga').fill_last_name('YA')
    registration_page.fill_email('name@example.com')
    registration_page.fill_gender('Female')
    registration_page.fill_mobile('8922569476')
    registration_page.fill_date_of_birth('1999', 'May', '11')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies('Reading')
    registration_page.fill_picture('tests.jpg')
    registration_page.fill_current_address('Moscowskaya Street 18')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')
    registration_page.fill_submit()




    # THEN
    registration_page.should_registered_user_with(
        'Olga YA',
        'name@example.com',
        'Female',
        '8922569476',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'tests.jpg',
        'Moscowskaya Street 18',
        'Haryana Karnal'
    )
