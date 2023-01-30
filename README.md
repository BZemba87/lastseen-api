#                               LAST SEEN

This API is the backend service for a social media image sharing platform called Last Seen.

# Development Goals 

The goal of this API is to provide a backend service to allow the Last Seen front end application to perform Create, Read, Update and Delete operations via the UI.

# Developer Goals and User Stories
- As a developer, I want to create a Profiles Model so that users can create a profile

- As a developer, I want to create a Posts Model so that logged in users can create, read, update and delete a post and logged out users can read a post

- As a developer, I want to create a Likes Model so that logged in users can like and unlike a post 

- As a developer, I want to create a Comments Model so that logged in users can create, read, update and delete a comment and logged out users can read a comment.

- As a developer, I want to create a search function so users can search for posts by post title or username

# Developer Goals - Tests
- As a developer, I want to create a Profiles Model so that users can create a profile

In Profiles models.py, a signal was created in order to create a new user profile on signup.

- As a developer, I want to create a Posts Model so that logged in users can create, read, update and delete a post and logged out users can read a post

Users can create, read, update and delete a post successfully and logged out users can read a post.

- As a developer, I want to create a Likes Model so that logged in users can like and unlike a post

Only logged in users can successfully like and unlike a post.  

- As a developer, I want to create a Comments Model so that logged in users can create, read, update and delete a comment and logged out users can read a comment.

Logged in users can create, read, update and delete comments and logged out users can only read comments.

- As a developer, I want to create a search function so logged in/out users can search for posts by post title or username

Users can successfully search for posts by post title or username regardless of whether they are logged in or out.

# Security 

A permissions class was added to views.py for Profiles, Posts and Comments apps called IsOwnerOrReadOnly to ensure only users who are owners of the profile, post or comment are able to update or delete.

# Technologies
- Django REST Framework
- ElephantSQL
- Cloudinary 
- Heroku
- Gitpod
- Github

# Deployment
- This API is deployed to Heroku. Please follow the steps below:

- Fork or clone this repository in GitHub

- Create a Cloudinary account to store images/static files and log in

- Click on 'Dashboard'

- Copy the value of the 'API Environment variable' link

- Log in to Heroku

- Click on 'New' and select 'Create new app' from the dropdown

- Enter a name for the app and select the appropriate region

- Select 'Create app'

- Click on 'Settings'

- Log in to ElephantSQL (with Github)

- Click 'Create New Instance' on the dashboard

- Create a name and select the 'Tiny Turtle (Free)' plan

- Click 'Select Region'

- Choose the nearest data centre to your location

- Click 'Review'

- Go to the ElephantSQL dashboard and click on the name of this project listed under 'Instances'

- Copy the ElephantSQL database URL

- Return to Heroku

- Click on the 'Settings' tab

- Scroll down and click on 'Reveal Config Vars'

### Enter the following config var names and values: 

- CLOUDINARY_URL: your cloudinary URL as obtained above 

- DATABASE_URL: your ElephantSQL postgres database URL as obtained above 

- SECRET_KEY

- Click the 'Deploy' tab

- Select 'GitHub' and confirm you wish to deploy using GitHub

- Find the 'Connect to GitHub' section and use the search box to locate relevant repo

- Select 'Connect'

- If you would like your site to be automatically deployed with each change that is pushed to Github, choose the 'main' branch under 'Automatic Deploys' and select 'Enable Automatic Deploys'

- Alternatively, you can select 'Manual Deploy' below and choose 'main' as the branch to deploy and select 'Deploy Branch'. Your site will only be manually deployed when you choose

- Once the deployment process is complete, you will be able to click on a link to your deployed site

## To connect the front end site to the back end on Heroku and Gitpod:

- Add new config var to API on Heroku called CLIENT_ORIGIN with a value of the url for the deployed React project 

- Add a CLIENT_ORIGIN_DEV key with the value of your Gitpod preview link

- Now we need to tell our React project to send requests to the API

- To do this, install the Axios Library in your Gitpod workspace

- Create an api folder with an axiosDefaults file inside it and import axios

- Now add base_URL of your deployed API project 

- Set the content-type header to multipart/form-data 

- Set withCredentials to true

- Import them into App.js

# Credit

- Code Institute Django REST Framework walkthrough
- Slack
- Mentor 

















