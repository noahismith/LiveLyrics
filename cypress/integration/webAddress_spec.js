describe('checks for proper web address for each page', function () {
    it ('Visit contact page', function () {
        cy.visit('https://docs.google.com/forms/d/e/1FAIpQLSfkYm6pUmVJ7It-f96yoRxCMMzvktP9RRao0aAWooRUGMQW7Q/viewform?usp=sf_link')
    })

    it ('Visit home/login page', function () {
        cy.visit('localhost:5000')
    })

    it ('Visit lyrics page', function () {
        cy.visit('localhost:5000/lyrics')
    })

    it ('Visit songs page', function () {
        cy.visit('localhost:5000/songs')
    })

    it ('Visit users page', function () {
        cy.visit('localhost:5000/users')
    })
})