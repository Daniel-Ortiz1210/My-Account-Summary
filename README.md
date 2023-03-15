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

> - email (*string*)
	Destinatary email, you'll receive your account summary with this email
- account_number (*string*)
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

Check your email

Check your email inbox, and search for the email.
Download the csv file attached to the email.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Tabla centrada con estilo</title>

    <!-- Estilos para la tabla -->
    <style type="text/css">
        table {
            margin: 0 auto;
            border-collapse: collapse;
            width: 80%;
            max-width: 800px;
            border: 1px solid #ddd;
        }

        th, td {
            text-align: left;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        h1 {
            text-align: center;
        }

        img {
            height: 50px;
            margin: 20px;
        }

        body {
          font-family: 'Poppins', sans-serif;
          color: black;
        }
    </style>
</head>

<body>

    <!-- Coloca el logo aquí -->
    <img src="https://challenge-static-files.s3.amazonaws.com/logo_stori.png" alt="Stori Logo">

    <!-- Título de la tabla -->
    <h1>Aqui esta tu balance de cuenta</h1>

    <!-- Crea la tabla -->
    <table>
      <thead>
        <tr>
          <th>Balance Total</th>
          <th>Monto Promedio Crédito</th>
          <th>Monto Promedio Débito</th>
          <th>Transacciones por Mes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>200.00</td>
          <td>30.50</td>
          <td>-23.40</td>
          <td>Transacciones en enero: 10</td>
        </tr>
      </tbody>
    </table>

</body>
</html>
```
