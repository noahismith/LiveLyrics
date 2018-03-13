describe('While on the Users page, checks to make sure all inputs and buttons work', function () {

    it('Input text check for "Search for users"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('input').first().type('Example User Search Input')

    })

    it('Click submit button for user search (ensure it works)', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('form').first().submit()

    })

    it('Input text check for "New user"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('.newUserTest').type('Example New User Input')

    })

    it('Input text check for "New birthdate"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('.newBirthdateTest').type('01/01/1995')

    })

    it('Input text check for "New E-mail"', function () {
        cy.visit('127.0.0.1:5000/users')

        cy.get('.emailTest').type('livelyricshelp@gmail.com')

    })



    it('Search Test 1: Click submit button for search user without any input in text box (should return all users)', function () {
    
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click() 

        cy.visit('127.0.0.1:5000/users')
        
        cy.get('input').first().clear()
        cy.get('form').first().submit()

        cy.contains('LiveLyrics')

    })

    it('Search Test 2: Search for single user', function () {
    
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('LiveLyricsTest')
        cy.get('form').first().submit()

        cy.get('div').contains('LiveLyricsTest')
  
    })

    it('Search Test 3: Search for multiple users', function () {
   
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('LiveLyrics')
        cy.get('form').first().submit()

        cy.get('div').contains('LiveLyrics')
        cy.get('div').contains('LiveLyricsTest')
 
    })

    it('Search Test 4: Search for non-existent user', function () {
 
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('asddgohbnslaerkjghuepira')
        cy.get('form').first().submit()

        cy.get('div').should('not.contain', 'asddgohbnslaerkjghuepira')
  
    })

    it('Search Test 5: Search for user and click on their link for user information', function () {

        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/users')
        cy.get('input').first().type('LiveLyricsTest')
        cy.get('form').first().submit()

        cy.get('div').contains('LiveLyricsTest').click()
        cy.contains('Username: LiveLyricsTest')
        cy.contains('E-mail:')
        cy.contains('Birthdate:')
        cy.contains('Number of Contributions:')
 
    })
    
    it('Updating User Test: Update user\'s birthdate and email', function () {
  
        cy.visit('http://127.0.0.1:5000')
        cy.get('a').contains('Login').click()

        cy.visit('127.0.0.1:5000/users')
        
        cy.get('input.newUserTest').clear()
        cy.get('input.newBirthdateTest').clear()
        cy.get('input.emailTest').clear()

        cy.get('input.newUserTest').type('LiveLyrics')
        cy.get('input.newBirthdateTest').type('1995-01-01')
        cy.get('input.emailTest').type('LiveLyricsHelp@gmail.com')

        cy.get('form#editForm').first().submit()

    })

})