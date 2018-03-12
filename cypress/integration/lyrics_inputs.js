describe('While on the Lyrics page, checks to make sure all inputs and buttons work INDIVIDUALLY', function () {

    it('Input text check for "new song name"', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('input').first().type('Example New Song Input')

    })

    it('Input text check for "Lyrics"', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('.lyricsInputTest').type('Example Lyrics Input')

    })

    it('Input text check for "Track id"', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('.lyricsTrackIDTest').type('Example Track ID Input')

    })

    it('Input text check for "Timestamps"', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('.lyricsTimestampsTest').type('Example Timestamps Input')

    })

    it('Click submit button (ensure it works)', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('form').submit()

    })

    it('checks all inputs and submit at once', function () {
        cy.visit('http://localhost:5000/lyrics')

        cy.get('input').first().type('Example New Song Input')


        cy.get('.lyricsInputTest').type('Example Lyrics Input')


        cy.get('.lyricsTrackIDTest').type('Example Track ID Input')


        cy.get('.lyricsTimestampsTest').type('Example Timestamps Input')


        cy.get('form').submit()
    })
})
