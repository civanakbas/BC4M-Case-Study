![Tests](https://github.com/civanakbas/BC4M-Case-Study/actions/workflows/integration.yml/badge.svg)
![Deploy](https://github.com/civanakbas/BC4M-Case-Study/actions/workflows/deploy.yml/badge.svg)


# Instructions For Docker File

Run the commands
```
git clone https://github.com/civanakbas/BC4M-Case-Study.git
cd BC4M-Case-Study
docker build --tag bc4m/case:1.0 .
docker run -p 5000:5000 -e API_KEY=$API_KEY bc4m/case:1.0
```
and open [localhost:5000](http://localhost:5000/) on your browser.

You can use the API key I sent you in the email.

# Heroku

Visit the deployed site on [heroku](https://bc4m-case-study.herokuapp.com/).

Example call: https://bc4m-case-study.herokuapp.com/temperature?city=mugla

Note: The site may take a bit of time to load since the free tier dynos on Heroku sleeps after 30 mins of inactivity.

# Details

## Code

The API is developed using ```Flask```. There are some dummy tests written with ```pytest```. 

## integration.yml

The integration script runs when there is a pull request. It tests on ```ubuntu-latest``` with Python versions ``` 3.7, 3.8, 3.9, 3.10 ```. Builds the docker image and runs the tests with ```pytest```.

## deploy.yml

The deploy script runs when there is a push to the main branch. It has the same instructions with integration.yml file but it also deploys the app to ```heroku```.
