import threading; import time; 
import script; script = script.Commands()
#welcome screen
print("Welcome To Clicker Lite! \n"
      "\nCommands:\n" 
      "Set click speed by interval(sec) -> /setinterval <interval>\n"
      "Set click speed by clicks per second -> /setcps <cps>\n"
      "Enable/disable auto-clicking -> /on -- /off\n")
    
#input processing
def _process_input():
      while True:
            rawInput = input()
            inputs = rawInput.split(' ')
            _check_input(inputs)

#threading input
input_thread = threading.Thread(target=_process_input)
input_thread.daemon = True
input_thread.start()

#check for user input
def _check_input(inputs):
      #sets variables for user inputs for easy access
      user_input = inputs[0].lower()
      if len(inputs) > 1:
            value = inputs[1]
            
      if user_input == '/on':
            script.enable()
      elif user_input == '/off':
            script.disable()
      elif user_input == '/setinterval':
            try:
                  script.set_interval(float(value))
            except UnboundLocalError:
                  print("Invalid Input -> interval value not given")
      elif user_input == '/setcps':
            try:
                  script.set_cps(float(value))
            except UnboundLocalError:
                  print("Invalid Input -> cps value not given")
#actual program:
while True:
      if script.on == True:
            script.click()
            time.sleep(script.interval)