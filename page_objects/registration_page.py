import os

from selene import browser, have, command


class RegistrationPage:
    def __init__ (self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')

    def open (self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name (self, value):
        self.first_name.type(value)
        return self

    def fill_last_name (self, value):
        self.last_name.type(value)
        return self

    def fill_email (self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender (self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self


    def fill_mobile (self, value):
        browser.element('#userNumber').type(value)
        return self


    def fill_date_of_birth (self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self,value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self,value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def fill_picture (self,path):
        browser.element('#uploadPicture').send_keys(os.getcwd() + f'/{path}')
        return self

    def fill_current_address (self, value):
        browser.element('#currentAddress').type(value)
        return self


    def fill_state (self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city (self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_submit (self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_registered_user_with (self, full_name, email, gender,mobile,date_of_birth,subjects,hobbies,picture,current_address,state,city):
        # todo: refactor to reuse parameters
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state,
                city
            )
        )
        return self
