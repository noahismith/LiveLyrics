describe('While on the Users page, checks to make sure all inputs and buttons work', function () {

    it('Input text check for "Search for users"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('input').first().type('Example User Search Input')

    })

    it('Click submit button for user search (ensure it works)', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('form').first().submit()

    })

    it('Input text check for "New user"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('.newUserTest').type('Example New User Input')

    })

    it('Input text check for "New birthdate"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('.newBirthdateTest').type('01/01/1995')

    })

    it('Input text check for "New E-mail"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('.emailTest').type('livelyricshelp@gmail.com')

    })



    it('Click submit button for search user without any input in text box (string of zero length case)', function () {
        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().clear()

        cy.get('form').first().submit()

    })


})