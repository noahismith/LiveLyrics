
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

    it('Login Test 1: Check to see if a user is already logged in (Next test should fail if this test passes)', function () {
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()
    })

    it('Login Test 2: Input login info to Spotify API call (Fails means already logged in, try using your own Spotify credentials)', function () {
        cy.visit('https://accounts.spotify.com/en/authorize?scope=streaming%20user-read-playback-state%20user-modify-playback-state%20user-read-currently-playing%20user-read-email%20user-read-birthdate&redirect_uri=http:%2F%2F127.0.0.1:5000%2Flogin&response_type=code&client_id=91893049176646de8ec8994ea5cd0b27&show_dialog=false')
        cy.get('a').contains('Log in to Spotify').click()
        cy.get('input').first().type('LiveLyricsHelp@gmail.com')
        cy.get('input#login-password.form-control.input-with-feedback.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required').get('#login-password').type('cs408team11')
        cy.get('button').click()
    })

    it('Login Test 3: Check to see if a user is already logged in (This test should pass no matter the results of Login Test 1 and 2)', function () {
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()
    })

})