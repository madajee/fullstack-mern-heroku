https://medium.com/crowdbotics/deploy-a-mern-stack-app-on-heroku-b0c255744a70

npm start servers

heroku config:set MONGODB_URI=mongodb://user:password@ds125453.mlab.com:25453/mern-example -a damp-dusk-80048
heroku config:get MONGODB_URI --app damp-dusk-80048