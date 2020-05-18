# Lvlup payments

## Examples

#### Set api key
```python
setApiKey('yourapikey')
```
#### Payments list
```python
paymentsList(10)  # here 10 is limit of taked payments
``` 
#### Balance
```python
balance()['balancePlnInt']  # 'balancePlntInt' returns e.g 80085, when 'balancePlnFormatted' returns "800,85 PLN"
```
#### Transaction status
```python
checkPayment('VMBY3T510CV5FFMB')  # returns boolean, true if paid, false if not
```
#### Create payment
```python
createPayment(12.50, 'redirectUrl', 'webhookUrl')  #  only amount is required
```
