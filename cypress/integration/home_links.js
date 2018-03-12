describe('While on the home page, checks to make sure all navigation buttons go to the right link', function () {

    it('Click Lyrics menu button', function () {
        cy.visit('http://localhost:5000')

        cy.get('ul').contains('Lyrics').click()

        cy.url()
            .should('include', '/lyrics')
    })

    it('Click Users menu button', function () {
        cy.visit('http://localhost:5000')

        cy.get('a').contains('Users').click()

        cy.url()
            .should('include', '/users')
    })

    it('Click Songs menu button', function () {
        cy.visit('http://localhost:5000')

        cy.get('ul').contains('Songs').click()

        cy.url()
            .should('include', '/songs')
    })

    it('Click Login button', function () {
        cy.visit('http://localhost:5000')

        cy.get('a').contains('Login').click()
    })

    it('Click Contact Us menu button', function () {
        cy.visit('http://localhost:5000')

        cy.get('ul').contains('Contact Us').click()
    })

})