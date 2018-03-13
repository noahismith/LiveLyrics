
describe('While on the home page, checks to make sure all navigation buttons go to the right page', function () {

    it('Click Lyrics menu button (routes to Lyrics page)', function () {
        cy.visit('127.0.0.1:5000')

        cy.get('ul').contains('Lyrics').click()

        cy.url()
            .should('include', '/lyrics')
    })

    it('Click Users menu button (routes to User page)', function () {
        cy.visit('127.0.0.1:5000')

        cy.get('a').contains('Users').click()

        cy.url()
            .should('include', '/users')
    })

    it('Click Songs menu button (routes to Songs page)', function () {
        cy.visit('127.0.0.1:5000')

        cy.get('ul').contains('Songs').click()

        cy.url()
            .should('include', '/songs')
    })

    it('Click Login button (checks login successful)', function () {
        
        cy.visit('127.0.0.1:5000')

        cy.get('a').contains('Login').click()


    })


})