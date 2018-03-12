describe('While on the Songs page, checks to make sure all inputs and buttons work', function () {

    it('Input text check (ensure it takes input)', function () {
        cy.visit('http://localhost:5000/songs')

        cy.get('input').first().type('Example Song Input')

    })
    
    it('Click submit button (ensure it works)', function () {
        cy.visit('http://localhost:5000/songs')

        cy.get('form').submit()

    })
})