![Tests](https://github.com/civanakbas/BC4M-Case-Study/actions/workflows/integration.yml/badge.svg)
![Deploy](https://github.com/civanakbas/BC4M-Case-Study/actions/workflows/deploy.yml/badge.svg)


# Instructions For Docker File

Run the commands
```
git clone https://github.com/civanakbas/BC4M-Case-Study.git
docker build --tag bc4m/case:1.0 .
docker run -p 5000:5000 -e API_KEY bc4m/case:1.0
```
and open [localhost:5000](http://localhost:5000/) on your browser.

You can use the api key I sent you in the email.

or visit the deployed site on [heroku](https://bc4m-case-study.herokuapp.com/).

Example call: https://bc4m-case-study.herokuapp.com/temperature?city=mugla

Note: The site may take a bit of time to load since the free tier dynos on Heroku sleeps after 30 mins of inactivity.
