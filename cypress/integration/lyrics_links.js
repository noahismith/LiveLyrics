describe('While on the home page, checks to make sure all navigation buttons go to the right link', function () {

    it('Click Home menu button', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('ul').contains('Home').click()

        cy.url()
            .should('eq', 'http://localhost:5000/')
    })

    it('Click Users menu button', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('a').contains('Users').click()

        cy.url()
            .should('eq', 'http://localhost:5000/users')
    })

    it('Click Songs menu button', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('ul').contains('Songs').click()

        cy.url()
            .should('eq', 'http://localhost:5000/songs')
    })

    it('Click Contact Us menu button', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('ul').contains('Contact Us').click()
    })

})