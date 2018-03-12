describe('While on the Songs page, checks to make sure all navigation buttons go to the right link', function () {

    it('Click Home menu button', function () {
        cy.visit('http://localhost:5000/songs')

        cy.get('ul').contains('Home').click()

        cy.url()
            .should('eq', 'http://localhost:5000/')
    })

    it('Click Users menu button', function () {
        cy.visit('http://localhost:5000/songs')

        cy.get('ul').contains('Users').click()

        cy.url()
            .should('eq', 'http://localhost:5000/users')
    })

    it('Click Lyrics menu button', function () {
        cy.visit('http://localhost:5000/songs')

        cy.get('ul').contains('Add Lyrics').click()

        cy.url()
            .should('eq', 'http://localhost:5000/lyrics')
    })

    it('Click Contact Us menu button', function () {
        cy.visit('http://localhost:5000/songs')

        cy.get('ul').contains('Contact Us').click()
    })

})