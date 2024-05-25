import pyautogui as pyg 

class Commands:
    def __init__(self):
        #defaults values
        self.interval = 1 
        self.on = False
    
    #set click speed by interval
    def set_interval(self, interval): 
        self.interval = interval
        print("Interval set to: " + str(interval))
    
    #set click speed by cps
    def set_cps(self, cps): 
        self.interval = 1.0/cps
        print("Cps set to:  " + str(cps))
    #toggle clicking
    def enable(self):
        self.on = True
        print("Clicking...")
    
    #toggle clicking off
    def disable(self):
        self.on = False
        print("Program stopped")
    
    #click once
    def click(self):
        pyg.click()


#testing
cmd = Commands()

