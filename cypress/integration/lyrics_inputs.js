describe('While on the Lyrics page, checks to make sure all inputs and buttons work INDIVIDUALLY', function () {

    it('Input text check for "new song name"', function () {
        cy.visit('127.0.0.1:5000/lyrics')

        cy.get('input').first().type('Example New Song Input')

    })

    it('Input text check for "Lyrics"', function () {
        cy.visit('127.0.0.1:5000/lyrics')

        cy.get('.lyricsInputTest').type('Example Lyrics Input')

    })

    it('Input text check for "Track id"', function () {
        cy.visit('127.0.0.1:5000/lyrics')

        cy.get('.lyricsTrackIDTest').type('Example Track ID Input')

    })

    it('Input text check for "Timestamps"', function () {
        cy.visit('127.0.0.1:5000/lyrics')

        cy.get('.lyricsTimestampsTest').type('Example Timestamps Input')

    })

    it('Click submit button (ensure it works)', function () {
        cy.visit('127.0.0.1:5000/lyrics')

        cy.get('form').submit()

    })

    it('checks all inputs and submit at once', function () {
        cy.visit('127.0.0.1:5000/lyrics')

        cy.get('input').first().type('Example New Song Input')


        cy.get('.lyricsInputTest').type('Example Lyrics Input')


        cy.get('.lyricsTrackIDTest').type('Example Track ID Input')


        cy.get('.lyricsTimestampsTest').type('Example Timestamps Input')


        cy.get('form').submit()
    })

    it ('Login', function () {
        cy.visit('127.0.0.1:5000')
        cy.get('a').contains('Login').click()

    })

    it('Test Add: Add lyrics to song on Add Lyrics page (Part 1/3)', function () {
    
        cy.visit('127.0.0.1:5000')
        cy.get('a').contains('Login').click()


        cy.visit('127.0.0.1:5000/lyrics')


        cy.get('input').first().clear()
        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsTrackIDTest').clear()
        cy.get('.lyricsTimestampsTest').clear()

        cy.get('input').first().type('Hello')
        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('form').submit();


        cy.get('input').first().clear()
        cy.get('.lyricsTrackIDTest').clear()

        cy.get('input').first().type('Hello')

        cy.get('.lyricsInputTest').type('Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('.lyricsTimestampsTest').type('0:09')

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('example song')
        cy.get('form').submit()


    })

    it ('Test Add: Search for updated song on Songs page (Part 2/3)', function () {

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('example song')
        cy.get('form').submit()


    })
})
