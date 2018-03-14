describe('While on the Songs page, checks to make sure all inputs and buttons work', function () {

    it('Input text check (ensure it takes input)', function () {
      
        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Example Song Input')

    })
    
    it('Click submit button (ensure it works)', function () {
     
        cy.visit('127.0.0.1:5000/songs')

        cy.get('form').submit()

    })

    it('Check when song does not exist', function () {
      
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Example Song Input')

        cy.get('form').submit()

        cy.should('not.contain', 'Example Song Input').click()

    })

    it('Check when the song exists', function () {
      
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Hello')

        cy.get('form').submit()

        cy.get('div.indiv-song').get('a').contains('Hello').click()
    })
})