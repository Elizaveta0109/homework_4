from pathlib import Path
import pytest
from selene import browser, by, have, command


def test_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Elizaveta')
    browser.element('#lastName').type('Sytaya')
    browser.element('#userEmail').type('eliza@mail.ru')
    browser.element(by.text('Female')).click()
    browser.element('#userNumber').type('9831112233')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('September')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2000')).click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element(by.text('Music')).click()

    browser.element("#uploadPicture").perform(command.js.scroll_into_view)

    picture_path = str(Path(__file__).parent.joinpath('resources', 'picture.horse.jpg').resolve())
    browser.element('#uploadPicture').set_value(picture_path)

    browser.element('#currentAddress').type('Moscow')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )

    # Таблица с результатами
    browser.element('.table').all('tbody tr').should(
        have.exact_texts('Student Name Elizaveta Sytaya',
                         'Student Email eliza@mail.ru',
                         'Gender Female',
                         'Mobile 9831112233',
                         'Date of Birth 01 September,2000',
                         'Subjects Maths',
                         'Hobbies Music',
                         'Picture picture.horse.jpg',
                         'Address Moscow',
                         'State and City Haryana Karnal'))

