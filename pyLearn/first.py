import PySimpleGUI as sg
import requests

# Define the layout
col = [[sg.Text('What town will you be riding in today?', text_color='white', background_color='blue'), sg.Input(key='-CITY-')]]
layout = [[sg.Column(col, background_color='blue')],
        [sg.OK()]
]



# Create the window
window = sg.Window('Current Weather', layout, margins=(0, 0), element_padding=(0, 0))

# Read the window
event, values = window.read()

# If user closes the window or clicks OK
if event == sg.WIN_CLOSED or event == 'OK':
    user_input = values['-CITY-']  # Get the input value from the key '-CITY-'

    api_key = 'Hello World'
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.status_code == 200:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        layout2 = [[sg.Text(f"Weather in {user_input}", font = ("Helvetica", 40))],
        [sg.Text(f"Weather: {weather}", font = ("Helvetica", 20))],
        [sg.Text(f"Temperature: {temp}°F", font = ("Helvetica", 20))],
        [sg.OK()]
]



        # Display the weather information in a popup
        window2 = sg.Window('Current Weather', layout2, size = (480,320), element_justification="center", finalize = True)
        window2.Maximize()

        while True:
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED or event2 == 'OK':
                break

        window2.close()
        #sg.popup(f"Weather: {weather}", f"Temperature: {temp}°F")
    else:
        # Display an error message if the request was not successful
        sg.popup("Error fetching weather data. Please check the city name.")

    window.close()
