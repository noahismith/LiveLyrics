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

    it('Test case 003 / 004 / 008 (returning user): Logging in to LiveLyrics Account, Create Live Lyrics Account, and Link Media Account to LiveLyrics', function () {

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
        cy.get('input#timestamps-input.lyricsTimestampsTest').clear()

        /* test input of song, 'Hello', and track key, '0ENSn4fwAbCGeFGVUbXEU3' then submit */
        cy.get('input').first().type('Hello')
        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('form').first().submit();

        /* clear inputs for song and track key */
        cy.get('input').first().clear()
        cy.get('.lyricsTrackIDTest').clear()

        /* Fill song, lyrics, track key, and timestamp fields and submit */
        cy.get('input').first().type('Hello')

        cy.get('.lyricsInputTest').type('Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('input#timestamps-input.lyricsTimestampsTest').type('0:09')
        cy.get('form').first().submit()

    })

    it('Test case 001 (part2): Adding lyrics', function () {

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

        cy.get('input#timestamps-input.lyricsTimestampsTest').should('have.value', '0:09')

    })

    it('Test Case 005: View Contributed Lyrics', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* go to songs page */
        cy.visit('http://127.0.0.1:5000/songs')

        /* input search of 'Hello' and click link for song */
        cy.get('input').first().type('Hello')

        cy.get('form').submit()

        cy.get('div.indiv-song').get('a').contains('Hello').click()

    })

    it('Test Case 006: Rating Lyrics Page', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* go to songs page */
        cy.visit('http://127.0.0.1:5000/songs')

        /* input search of 'Hello' and click link for song */
        cy.get('input').first().type('Hello')

        cy.get('form').submit()
    
        cy.get('div.indiv-song').get('a').contains('Hello').click()

        /* rate the lyrics */
        cy.get('label.star').first().click()
        cy.get('button').contains('Submit Rating').click()

        /* WAIT FOR 3 SECONDS AT LEAST, OTHERWISE BLEEDS INTO TEST CASE 009 AND CAUSES FALSE FAILURE */
        cy.wait(4000)

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
        cy.get('div#searchResults').contains('LiveLyrics').click()
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
        cy.get('input').first().type('wojtr')
        cy.get('form').first().submit()

        /* click user name link to view user's information */
        cy.get('div').contains('wojtr').click()
        cy.contains('Username: wojtr')
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

    it('Test Case 016: User searches for an invalid user', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('asddgohbnslaerkjghuepira')
        cy.get('form').first().submit()

        cy.get('div').should('not.contain', 'asddgohbnslaerkjghuepira')

    })

    it('Test Case 017: User searches for lyrics that do not exist', function () {

        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Example Song Input')

        cy.get('form').submit()

        cy.should('not.contain', 'Example Song Input').click()

    })

    it ('Test Case 019 / 020: User tries to add lyrics that they have already added before', function () {
   
        /* ensure logged in and have Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('http://127.0.0.1:5000/lyrics')


        cy.get('input').first().clear()
        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsTrackIDTest').clear()
        cy.get('input#timestamps-input.lyricsTimestampsTest').clear()

        cy.get('input').first().type('Hello')
        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('form').first().submit();


        cy.get('input').first().clear()
        cy.get('.lyricsTrackIDTest').clear()

        cy.get('input').first().type('Hello')

        cy.get('.lyricsInputTest').type('Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('input#timestamps-input.lyricsTimestampsTest').type('0:09')
        cy.get('form').first().submit()


        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Hello')
        cy.get('form').first().submit()

        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()


        cy.get('input#song-title-input').should('have.value', 'Hello')
        cy.get('.lyricsInputTest').should('have.value', 'Hello, it\'s me. I was wondereing if after all these years you\'d like to meet.')

        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsInputTest').type('Hello, it\'s me. I was wondereing if after all these years you\'d like to meet. To go over everything. They say it\'s supposed to heal.')

        cy.get('.lyricsTrackIDTest').should('have.value', '0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('input#timestamps-input.lyricsTimestampsTest').clear()
        cy.get('input#timestamps-input.lyricsTimestampsTest').type('0:09 0:12')
        cy.get('form').first().submit()

        /* keeps program from false failure due to race case */
        cy.wait(5000)

        cy.visit('127.0.0.1:5000/songs')

        cy.get('input').first().type('Hello')
        cy.get('form').first().submit()

        cy.get('div.indiv-song').contains('0ENSn4fwAbCGeFGVUbXEU3').get('a').contains('Hello').click()

        cy.get('input#song-title-input').should('have.value', 'Hello')

        cy.get('.lyricsInputTest').should('have.value', 'Hello, it\'s me. I was wondereing if after all these years you\'d like to meet. To go over everything. They say it\'s supposed to heal.')

        cy.get('.lyricsTrackIDTest').should('have.value', '0ENSn4fwAbCGeFGVUbXEU3')

        cy.get('input#timestamps-input.lyricsTimestampsTest').should('have.value', '0:09 0:12')

        /* keeps program from false failure due to race case */
        cy.wait(5000)

    })

    it('Test Case 022: User tries to access the Live Lyrics', function () {

        cy.wait(5000)

        /* Ensure user is logged in (shouldn't matter in this case) */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* Check Home route from Add Lyrics page */
        cy.visit('http://127.0.0.1:5000/lyrics')

        cy.get('a').contains('LiveLyrics').click()

        cy.url()
            .should('eq', 'http://127.0.0.1:5000/')

        /* Check Home route from Users page */
        cy.visit('http://127.0.0.1:5000/users')

        cy.get('a').contains('LiveLyrics').click()

        cy.url()
            .should('eq', 'http://127.0.0.1:5000/')

        /* Check Home route from Songs page */
        cy.visit('http://127.0.0.1:5000/songs')

        cy.get('a').contains('LiveLyrics').click()

        cy.url()
            .should('eq', 'http://127.0.0.1:5000/')

    })

    it('Test Case 023: Recent contributions are updated correctly and consistently', function () {

        /* Ensure user is logged in (shouldn't matter in this case) */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        /* Ensure username by setting it on User page */
        cy.visit('http://127.0.0.1:5000/users')
        
        cy.get('input.newUserTest').clear()

        cy.get('input.newUserTest').type('LiveLyrics')

        cy.get('form#editForm').first().submit()

        /* Add lyrics to song */
        cy.visit('http://127.0.0.1:5000/lyrics')

        /* Clear all previous values */
        cy.get('input').first().clear()
        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsTrackIDTest').clear()
        cy.get('input#timestamps-input.lyricsTimestampsTest').clear()

        /* Insert new values and post */
        cy.get('input').first().type('Hello')
        cy.get('.lyricsInputTest').type('Hello, it\'s me\n I was wondering if after all these years you\'d like to meet\n To go over everything\n They say that time\'s supposed to heal ya\n But I ain\'t done much healing')
        cy.get('.lyricsTrackIDTest').type('0ENSn4fwAbCGeFGVUbXEU3')
        cy.get('input#timestamps-input.lyricsTimestampsTest').type('0:09 0:13')

        cy.get('form').first().submit();

        /* Check the recent activities most recent post to see if it matches */
        cy.visit('http://127.0.0.1:5000/activity')

        cy.get('div#activity-feed').get('span').first().should('contain', 'Song: Hello')


        /* Add another set of lyrics to a song */
        cy.visit('http://127.0.0.1:5000/lyrics')

        /* Clear all previous values */
        cy.get('input').first().clear()
        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsTrackIDTest').clear()
        cy.get('input#timestamps-input.lyricsTimestampsTest').clear()

        /* Insert new values and post */
        cy.get('input').first().type('Juicy')
        cy.get('.lyricsInputTest').type('Yea, this album is dedicated to all the teachers that told me I\'d never amount to nothing.')
        cy.get('.lyricsTrackIDTest').type('5ByAIlEEnxYdvpnezg7HTX')

        cy.get('form').first().submit();

        /* stops race case from failing test case */
        cy.wait(3000)

        /* Check the recent activities most recent post to see if it matches */
        cy.visit('http://127.0.0.1:5000/activity')

        cy.get('div#activity-feed').get('span').first().should('contain', 'Song: Juicy')

        /* Overkill test to ensure most recent post is not actually second newest post */
        cy.get('div#activity-feed').get('span').first().should('not.contain', '-- Song: Hello')


        /* Add 3rd set of lyrics to a song (For good measure) */
        cy.visit('http://127.0.0.1:5000/lyrics')

        /* Clear all previous values */
        cy.get('input').first().clear()
        cy.get('.lyricsInputTest').clear()
        cy.get('.lyricsTrackIDTest').clear()
        cy.get('input#timestamps-input.lyricsTimestampsTest').clear()

        /* Insert new values and post */
        cy.get('input').first().type('Love Train')
        cy.get('.lyricsInputTest').type('People all over the world Join hands')
        cy.get('.lyricsTrackIDTest').type('28285KFbyCq8sJofn58qlD')

        cy.get('form').first().submit();

        /* Check the recent activities most recent post to see if it matches */
        cy.visit('http://127.0.0.1:5000/activity')

        cy.get('div#activity-feed').get('span').first().should('contain', 'Song: Love Train')

        /* Overkill test to ensure most recent post is not actually second newest post */
        cy.get('div#activity-feed').get('span').first().should('not.contain', '-- Song: Juicy')

        cy.wait(5000)
    })

    it('Test Case 025 / 026: User\'s own profile page and other users\' profile pages are updated correctly when statistics change', function () {

        /* Ensure user has Spotify token */
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('http://127.0.0.1:5000/users')
        
        /* Clear credentials */
        cy.get('input.newUserTest').clear()
        cy.get('input.emailTest').clear()

        /* Set default credentials */
        cy.get('input.newUserTest').type('LiveLyricsTest1')
        cy.get('input.emailTest').type('LiveLyricsHelp1@gmail.com')

        cy.get('form#editForm').first().submit()

        /* Check that the default credentials were set */
        cy.visit('http://127.0.0.1:5000/users')
        cy.get('input').first().type('LiveLyricsTest1')
        cy.get('form').first().submit()

        cy.get('div').contains('LiveLyricsTest1').click()
        cy.contains('Username: LiveLyricsTest1')
        cy.contains('E-mail: LiveLyricsHelp1@gmail.com')
        cy.contains('Birthdate:')
        cy.contains('Number of Contributions:')

        /* Change default credentials */
        cy.visit('http://127.0.0.1:5000/users')
        cy.get('input.newUserTest').clear()
        cy.get('input.emailTest').clear()

        cy.get('input.newUserTest').type('LiveLyricsTest2')
        cy.get('input.emailTest').type('LiveLyricsHelp2@gmail.com')

        cy.get('form#editForm').first().submit()

        /* Check that the changes were saved */
        cy.visit('http://127.0.0.1:5000/users')
        cy.get('input').first().type('LiveLyricsTest2')
        cy.get('form').first().submit()

        cy.get('div').contains('LiveLyricsTest2').click()
        cy.contains('Username: LiveLyricsTest2')
        cy.contains('E-mail: LiveLyricsHelp2@gmail.com')
        cy.contains('Birthdate:')
        cy.contains('Number of Contributions:')

    })

})