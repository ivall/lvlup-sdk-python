# Lvlup payments

## Examples

#### New instance
```python
payment = Payments('api_key')
```
#### Payments
```python
payment.payments(10)  # here 10 is limit of taked payments
``` 
#### Balance
```python
payment.balance()['balancePlnInt']  # 'balancePlntInt' returns e.g 80085, when 'balancePlnFormatted' returns "800,85 PLN"
```
#### Transaction status
```python
payment.is_payed('VMBY3T510CV5FFMB')  # returns boolean, true if paid, false if not
```
#### Create payment
```python
payment.create_payment(12.55, 'redirectUrl', 'webhookUrl')  #  only amount is required
```
