import os

from selene import browser, have, command

from data.users import User


class RegistrationPage:

    def open (self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def simle_register (self, student: User):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.all('[name=gender]').element_by(have.value(student.gender)).element('..').click()
        browser.element('#userNumber').type(student.mobile)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(student.month)
        browser.element('.react-datepicker__year-select').type(student.year)
        browser.element(
            f'.react-datepicker__day--0{student.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element('#subjectsInput').type(student.subjects).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(student.hobbies)).click()
        browser.element('#uploadPicture').send_keys(os.getcwd() + f'/{student.picture}')
        browser.element('#currentAddress').type(student.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.city)).click()
        browser.element('#submit').perform(command.js.click)


    def should_registered_user (self, student):
        full_name = f'{student.first_name} {student.last_name}'
        birthday = f'{student.day} {student.month},{student.year}'
        state_city = f'{student.state} {student.city}'
        browser.element('.table').all('td').even.should( have.exact_texts(
            full_name,
            student.email,
            student.gender,
            student.mobile,
            birthday,
            student.subjects,
            student.hobbies,
            student.picture,
            student.address,
            state_city)
        )







