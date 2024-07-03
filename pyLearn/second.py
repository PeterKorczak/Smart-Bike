import PySimpleGUI as sg
import requests




sg.theme('BlueMono')

# Column layout
col = [[sg.Text('What town will you be riding in today?', text_color='white', background_color='blue'), sg.Input('')]]
# Window layout
layout = [[sg.Column(col, background_color='blue')],
          [sg.OK()]]

# Display the window and get values
window = sg.Window('Column Element', layout, margins=(0,0), element_padding=(0,0))
event, values = window.read()


api_key = 'dedf0f08dee5dee7888cff5e1af013b9'
user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

#print(weather, temp)

sg.popup(weather, temp)
window.close()
