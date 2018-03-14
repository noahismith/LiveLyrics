describe('Front end test plan cases', function () {

    it('Test case 003 (new user): Logging in to LiveLyrics Account (Expected fail if returning user)', function () {
    
        cy.clearCookies()
        cy.getCookies().should('be.empty')
        cy.visit('https://accounts.spotify.com/en/authorize?scope=streaming%20user-read-playback-state%20user-modify-playback-state%20user-read-currently-playing%20user-read-email%20user-read-birthdate&redirect_uri=http:%2F%2F127.0.0.1:5000%2Flogin&response_type=code&client_id=91893049176646de8ec8994ea5cd0b27&show_dialog=false')
        cy.get('a').contains('Log in to Spotify').click()

        //REPLACE LiveLyricsHelp@gmail.com  WITH YOUR EMAIL TO TEST FIRST LOGIN
        cy.get('input').first().type('LiveLyricsHelp@gmail.com')

        //REPLACE cs408team11 WITH YOUR PASSWORD TO TEST FIRST LOGIN (WE DO NOT LOG YOUR PASSWORD AND WE WOULD NOT USE ANY OF YOUR LOGIN CREDENTIALS)
        cy.get('input#login-password.form-control.input-with-feedback.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required').get('#login-password').type('cs408team11')
        cy.get('button').click()

    })

    it('Test case 003 (returning user): Logging in to LiveLyrics Account', function () {

        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

    })

    it('Test case 001 (part 1): Adding lyrics', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('http://127.0.0.1:5000/lyrics')


        /* clear all inputs */
        cy.get('input').first().clear()
        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsTrackIDTest').clear()
        cy.get('.lyricsTimestampsTest').clear()

        /* test input of song, 'Hello', and track key, '0ENSn4fwAbCGeFGVUbXEU3' then submit */
        cy.get('input').first().type('Hello')
        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('form').submit();

        /* clear inputs for song and track key */
        cy.get('input').first().clear()
        cy.get('.lyricsTrackIDTest').clear()

        /* Fill song, lyrics, track key, and timestamp fields and submit */
        cy.get('input').first().type('Hello')

        cy.get('.lyricsInputTest').type('Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('.lyricsTimestampsTest').type('0:09')
        cy.get('form').submit()

    })

    it ('Test case 001 (part2): Adding lyrics', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        /* clear input and then search for song, 'Hello' */
        cy.get('input').first().clear()
        cy.get('input').first().type('Hello')
        cy.get('form').submit()

        /* click song link */
        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()


        /* check that previously entered song info updated and saved correctly */
        cy.get('input#song-title-input').should('have.value', 'Hello')

        cy.get('.lyricsInputTest').should('have.value', 'Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsTrackIDTest').should('have.value', '0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('.lyricsTimestampsTest').should('have.value', '0:09')

    })

    it ('Test Case 005: View Contributed Lyrics', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* go to songs page */
        cy.visit('127.0.0.1:5000/songs')

        /* input search of 'Hello' and click link for song */
        cy.get('input').first().type('Hello')

        cy.get('form').submit()

        cy.get('div.indiv-song').get('a').contains('Hello').click()

    })

    it('Test Case 009: User Profile Statistics', function () {

        /* LiveLyrics is the default user for testing */

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* search for 'LiveLyrics' user on user page */
        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('LiveLyrics')
        cy.get('form').first().submit()

        /* click user name link to view user's information */
        cy.get('div').contains('LiveLyrics').click()
        cy.contains('Username: LiveLyrics')
        cy.contains('E-mail:')
        cy.contains('Birthdate:')
        cy.contains('Number of Contributions:')

    })

    it('Test Case 010: View Other User’s Statistics', function () {

        /* LiveLyricsTest is the default other user for testing */

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* search for 'LiveLyricsTest' user on user page */
        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('LiveLyricsTest')
        cy.get('form').first().submit()

        /* click user name link to view user's information */
        cy.get('div').contains('LiveLyricsTest').click()
        cy.contains('Username: LiveLyricsTest')
        cy.contains('E-mail:')
        cy.contains('Birthdate:')
        cy.contains('Number of Contributions:')

    })

    it('Test Case 011: Report Issues', function () {

        /* check link from Home page */
        cy.visit('http://127.0.0.1:5000')
        cy.get('ul').contains('Contact Us').click()

        /* check link from Add Lyrics page */
        cy.visit('http://127.0.0.1:5000/lyrics')
        cy.get('ul').contains('Contact Us').click()

        /* check link from Users page */
        cy.visit('http://127.0.0.1:5000/users')
        cy.get('ul').contains('Contact Us').click()

        /* check link from Songs page */
        cy.visit('http://127.0.0.1:5000/songs')
        cy.get('ul').contains('Contact Us').click()

    })

    it('Test Case 015: Nothing is typed into the search bar', function () {
        
    })

    it('Test Case 016: User searches for an invalid user', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('asddgohbnslaerkjghuepira')
        cy.get('form').first().submit()

        cy.get('div').should('not.contain', 'asddgohbnslaerkjghuepira')

    })

    it('Test Case 017: User searches for lyrics that do not', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Example Song Input')

        cy.get('form').submit()

        cy.should('not.contain', 'Example Song Input').click()

    })

    it ('Test Case 019 / 020: User tries to add lyrics that they', function () {
   
        /* ensure logged in and have Spotify token */
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

    it('Test Case 022: User tries to access the Live Lyrics', function () {

        /* Ensure user is logged in (shouldn't matter in this case) */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* Check Home route from Add Lyrics page */
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('a').contains('LiveLyrics').click()

        cy.url()
            .should('eq', '127.0.0.1:5000')

        /* Check Home route from Users page */
        cy.visit('http://127.0.0.1:5000/users')

        cy.get('a').contains('LiveLyrics').click()

        cy.url()
            .should('eq', '127.0.0.1:5000')

        /* Check Home route from Songs page */
        cy.visit('http://127.0.0.1:5000/songs')

        cy.get('a').contains('LiveLyrics').click()

        cy.url()
            .should('eq', '127.0.0.1:5000')

    })

})