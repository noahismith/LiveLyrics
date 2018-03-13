describe('While on the Users page, checks to make sure all navigation buttons go to the right link', function () {

    it('Click Home menu button', function () {
        cy.visit('http://127.0.0.1:5000/users')

        cy.get('ul').contains('Home').click()

        cy.url()
            .should('eq', 'http://127.0.0.1:5000/')
    })

    it('Click Songs menu button', function () {
        cy.visit('http://127.0.0.1:5000/users')

        cy.get('ul').contains('Songs').click()

        cy.url()
            .should('eq', 'http://127.0.0.1:5000/songs')
    })

    it('Click Lyrics menu button', function () {
        cy.visit('http://127.0.0.1:5000/users')

        cy.get('ul').contains('Add Lyrics').click()

        cy.url()
            .should('eq', 'http://127.0.0.1:5000/lyrics')
    })

    it('Click Contact Us menu button', function () {
        cy.visit('http://127.0.0.1:5000/users')

        cy.get('ul').contains('Contact Us').click()
    })

})