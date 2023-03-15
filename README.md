# My Account Summary

I love buy all the things I need with my own money, but when it´s time to watch the numbers in my card, I want no surprises. Clear numbers beetween you and your bank is a key for a long relation.

## Installation

**Clone the repository to your local machine**

https://github.com/Daniel-Ortiz1210/My-Account-Summary.git

**Install Docker**

https://docs.docker.com/desktop/

## Usage

### Docker Compose

Move to the local repository in your machine
```bash
cd My-Account-Summary
```
Build the services with Docker Compose
```bash
docker-compose build
```
Run the container
```bash
docker-compose up -d
```

### Make a request

Once the container is up and running, you can use Postman to make a request.

#### Request example

http://0.0.0.0:8080/my_account_statement/{email}/{account_number}

> - **email** (*string*)
	Destinatary email, you'll receive your account summary with this email
> - **account_number** (*string*)
	Is a random 16-digit number, simulating a account number.

#### Responses

**200:**
```json
	{
	"message": "Email enviado con exito"
	}
```
**404:**
```json
	 {
	 "message": "No pudimos verificar tu numero cuenta"
	}
```
**400:**
```json
	{
	"message": "No pudimos enviar el correo electrónico"
	}
```

## Check your email

- Check your email inbox, and search for the email.
- Download the csv file attached to the email.

Now you can see a table with a summary of your lasts transactions, your account balance and more.

Enjoy!
