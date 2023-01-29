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

# Issues
- 















