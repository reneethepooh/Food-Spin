# Food-Spin

## Development Configuration
- Install the required packages from requirements.txt
- Modify db/my.cnf to whatever the credentials are for your MySQL database instance (I left mine in so you can see the format)

Reference this for using javascript:
https://stackoverflow.com/questions/15491727/include-css-and-javascript-in-my-django-template


## Deployment
We encountered a plethora of issues deploying our application on Amazon Beanstalk. As a result, we decided to deploy on university servers the application while still mantaining the initial objective of having a separate sql server on Amazon that is based on sharding. 
