# My Account Summary

I love buy all the things I need with my own money, but when it´s time to watch the numbers in my card, I want no surprises. Clear numbers beetween you and your bank is a key for a long relation.

## About the project
When you make a request, you dont have to worry about having to pass-in a set of transactions or a real account number. 
The API generate a set of 30 transactions in a 4 months period. The import and the date are randomly generated.
Then, the API inserts the transactions in our DB located in a public cloud, we use a PostgreSQL RDS database. (you can check the credentials in the docker-compose.yml file)
The API the process the transactions data and make an account summary, the send you later will see in the email.
We retrive the account summary and insert de data into an email template.
Finally, the API uses the SendGrid API to send the email with the csv file attached.

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
