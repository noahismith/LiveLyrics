describe('Login as a user (Fails if user has been logged in before)', function () {
    it('Login Test 2: Input login info to Spotify API call (Fails means already logged in, try using your own Spotify credentials)', function () {
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
})