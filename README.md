# Url Shortner
This is a Django based Url Shortner.
How To Setup:
1. On Heroku

a) Create an account on heroku Or login to your existing account

Then use this button to use this template.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/the-e3n/urlshortner)

b) Go to your your heroku app settings 
and add a variable named <code>SERVER</code> and enter value as the url of your app.

For example:- <code>https://onbit.herokuapp.com/</code> 

*The end <code>'/'</code> is necessary

c) Your app has been Deployed. 

*Remember Heroku resets its dyno every 24hrs so your urls will be removed


#Usage
1) Go to https://yourapp.herokuapp.com/ to create new URLS.


2) Go to https://yourapp.herokuapp.com/list to list all URLS and delete any existing URLS.

3) Go to http://yourapp.herokuapp.com/admin to enter admin app. default password is 1523 and useename is e3n











2. On Your Local Machine

<code>git clone https://github.com/the-e3n/urlshortner</code>

<code>cd url-shortner</code>

<code>pip install -r requirements.txt</code>

<code>python manage.py runserver</code>
