# Building a next best action model using machine learning model.
### Demo 
Link : https://customerstate.herokuapp.com/
### Overview
#### This is a simple classification Flask app developed with sklearn library. The model takes customer informationas input and it flooded into the trained model and it will predict the customer state that is churn or active.
### Goals
#### Primary Goal :The main to increase the Click Through Rate (CTR) or Conversion Rate (CR) (from Churn customer to Active customer) for a particular customer by reccomending the right products.
#### This can be achieved by dividing the whole project into 2 stages:
#### Stage 1 : Segregating the customer into two categories churn customer or active customer.
#### Stage 2 : Once the model is accurately able to segregate the customers into 2 categories, next stage is to classify them into further groups , so that the model can recommend right product and services to a customer.
### Methodology
#### Methidology Used : AGILE CRISP-DM METHODOLOGY
#### AGILE CRISP-DM :Cross Industry Standard Process for Data Mining (CRISP-DM), which has been in practice since 1997, is a data mining process model. It is a robust and proven methodology for guidance. This framework is tool-agnostic and application/industry neutral. The main advantage of going with CRISP-DM is it focuses on business problems as well as data analysis. We could bring together agile and scrum with CRISP-DM to make sense of data transformation.
* Meet with key stakeholders to get the vision and value for the data transformation
* Identify the team and roles – product owner, scrum master, data scientist, business analyst, SME, lead, and data developers.
* Identify the sprint length that is suitable for the organization and the project.
* Set up the baseline architecture, continuous integration architecture, and framework for deployments.
* Set up project infrastructure and conventions, schedule project activity and track and report progress.
### Technical Aspect
#### This project is divided into two part:
#### Training a machine learning model using sklearn. 
#### Building and hosting a Flask web app on Heroku.
### Model building and Evaluation
#### The precision and recall values of the classification model should be high so that the algorithm learn better and classify the customer correctly. Tried various machine algorithams and methods, based on the precision and recall value of model we chose Gradient Boosting model.
### Deployement on Heroku
#### web app has been deployed on Heroku.
Link : https://customerstate.herokuapp.com/
### Next plan?
#### The model has been passed to UAT (User Acceptance test ). Once the UAT process is done we are palnning to release the model into production environment and monitor for couple of months.
