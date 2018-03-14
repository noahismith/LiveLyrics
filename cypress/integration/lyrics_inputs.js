describe('While on the Lyrics page, checks to make sure all inputs and buttons work', function () {

    it('Input text check for "new song name"', function () {
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('input').first().type('Example New Song Input')

    })

    it('Input text check for "Lyrics"', function () {
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('.lyricsInputTest').type('Example Lyrics Input')

    })

    it('Input text check for "Track id"', function () {
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('.lyricsTrackIDTest').type('Example Track ID Input')

    })

    it('Input text check for "Timestamps"', function () {
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('.lyricsTimestampsTest').type('Example Timestamps Input')

    })

    it('Click submit button (ensure it works)', function () {
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('form').submit()

    })

    it('checks all inputs and submit at once', function () {
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('input').first().type('Example New Song Input')


        cy.get('.lyricsInputTest').type('Example Lyrics Input')


        cy.get('.lyricsTrackIDTest').type('Example Track ID Input')


        cy.get('.lyricsTimestampsTest').type('Example Timestamps Input')


        cy.get('form').submit()
    })

    it('Test Add 1: Add lyrics to song on Add Lyrics page (Part 1)', function () {

        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('http://127.0.0.1:5000/lyrics')


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
        cy.get('form').submit()

    })

    it ('Test Add 2: Search for updated song on Songs page and check that changes saved (Part 2)', function () {

        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().clear()
        cy.get('input').first().type('Hello')
        cy.get('form').submit()

        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()


        cy.get('input#song-title-input').should('have.value', 'Hello')

        cy.get('.lyricsInputTest').should('have.value', 'Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsTrackIDTest').should('have.value', '0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('.lyricsTimestampsTest').should('have.value', '0:09')

    })

    it('Test Update: Update lyrics and timestamps of a song', function () {

        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('http://127.0.0.1:5000/lyrics')


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
        cy.get('form').submit()


        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Hello')
        cy.get('form').submit()

        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()


        cy.get('input#song-title-input').should('have.value', 'Hello')
        cy.get('.lyricsInputTest').should('have.value', 'Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsInputTest').type('Hello, it\'s me. I was wondereing if after all these years you\'d like to meet. To go over everything. They say it\'s supposed to heal.')

        cy.get('.lyricsTrackIDTest').should('have.value', '0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('.lyricsTimestampsTest').clear()
        cy.get('.lyricsTimestampsTest').type('0:09 0:12')
        cy.get('form').submit()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Hello')
        cy.get('form').submit()

        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()

        cy.get('input#song-title-input').should('have.value', 'Hello')

        cy.get('.lyricsInputTest').should('have.value', 'Hello, it\'s me. I was wondereing if after all these years you\'d like to meet. To go over everything. They say it\'s supposed to heal.')

        cy.get('.lyricsTrackIDTest').should('have.value', '0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('.lyricsTimestampsTest').should('have.value', '0:09 0:12')

    })

    it('Adding a song not on spotify (should not be possible)', function () {

        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('input').first().clear()
        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsTrackIDTest').clear()
        cy.get('.lyricsTimestampsTest').clear()

        cy.get('input').first().type('Not on Spotify')

        cy.get('.lyricsTrackIDTest').type('abc123')

        cy.get('form').submit();

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Not on Spotify')
        cy.get('form').submit()

        cy.should('not.contain', 'Not on Spotify')
    })

    it('Changing a songs name', function () {

        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('http://127.0.0.1:5000/songs')

        cy.get('input').first().clear()
        cy.get('input').first().clear().type('Hello')
        cy.get('form').submit()
        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()

        cy.get('input').first().clear()
        cy.get('input').first().clear().type('NewHello')
        cy.get('form').submit()

        cy.visit('http://127.0.0.1:5000/songs')

        cy.get('input').first().clear().type('NewHello')
        cy.get('form').submit()
        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('NewHello').click()

        cy.get('input#song-title-input').should('have.value', 'NewHello')

        cy.get('input').first().clear()
        cy.get('input').first().clear().type('Hello')
        cy.get('form').submit()

        cy.visit('http://127.0.0.1:5000/songs')

        cy.get('input').first().clear()
        cy.get('input').first().clear().type('Hello')
        cy.get('form').submit()
        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()

        cy.get('input#song-title-input').should('have.value', 'Hello')

    })

})
