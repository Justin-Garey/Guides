# Using Google SMTP 

Don't host your own email server. It's apparently a futile effort with lots of headache.

This is useful for services with configurable mail server settings. I created a new gmail account for this. To set up the account for mail server access:
- Go to [account settings](https://myaccount.google.com/)
  - Enable 2-Step Verification
    - Found under Security & sign-in
  - Create an App Password for your applications login information
    - Search App Passwords in the search bar. 
    - Create an App Password by just typing in a name for the application and copying the generated key.

Google SMTP Settings
- Server Address: smtp.gmail.com
- Username: Your Email
- Password: The Generated App Password
- TLS Port: 587
- SSL Port: 465
- Security: TLS or SSL