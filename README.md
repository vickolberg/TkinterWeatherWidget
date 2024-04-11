This is a small widget application built using Python3 and Tkinter.

This application asks for user input, specifically your zip code, state, and country. 

Based on the user input, the application creates an API request URL to http://api.openweathermap.org/geo/1.0/. This API request converts the zip code and country code into latitude and longitude coordinates.

Once we have gathered the proper latitude and longitude coordinates, the next API call is made using https://api.openweathermap.org/data/2.5/weather. This will gather weather data for the given coordinates.

Once the api calls have been made, the tkinter widget will pop up with your city name, current temperature, todays high temperature, todays low temperature, and the time of sunrise and sunset.

This is a very basic application that has plenty of room for additions and changes. 
