from tkinter import *
from tkinter import ttk

#Attributes for the window
root = Tk()
root.title('Calorie Measure | Main Menu')
root.geometry("500x500")

class RecordingFitnessActivity:
    def __init__(self):
        #Creates the frame for the new window
        self.win = Toplevel() 
        self.frameFit = Frame(self.win)
        self.frameFit.pack()

        #Label that creates a title
        self.fitTitleLabel = Label(self.frameFit, text = "Record Fitness Activity")
        self.fitTitleLabel.pack()   

        #A comboBox that contains four fitness activites
        self.fitnessActivities = ["Walking", "Jogging", "Cycling", "Swimming"]
        self.activityCombo = ttk.Combobox(self.frameFit, value = self.fitnessActivities )
        self.activityCombo.current(0)
        self.activityCombo.bind("<<ComboboxSelected>>")
        self.activityCombo.pack()
        
        #Asks the user for Hours spented in activity
        self.hourLabel = Label(self.frameFit, text = "Enter the amount of Hours here:").pack()
        self.hourTxt = Entry(self.frameFit, width = 5)
        self.hourTxt.pack()

        #Asks the user for Minutes spented in activity
        Label(self.frameFit, text = "Enter the amount of Minutes here:").pack()
        self.minuteTxt = Entry(self.frameFit, width = 5)
        self.minuteTxt.pack()

        #Asks the user for their weight
        Label(self.frameFit, text = "Enter your in pounds (lb):").pack()
        self.userWeight = Entry(self.frameFit, width = 5)
        self.userWeight.pack()

        #Submits the information to a module called activityAndTime
        self.recordBtn = Button(self.frameFit, text = "Record Activity", command = self.activityAndTime)
        self.recordBtn.pack() 


    #This calculates the amount of calories burned from an activity
    def activityAndTime(self):
        
        #Creates variables to be used in this module
        self.fitActivty = self.activityCombo.get()
        self.hourAmount = int(self.hourTxt.get())
        self.minuteAmount = int(self.minuteTxt.get())
        self.weight = float(self.userWeight.get())

        #If the user entered more than 60 minutes, it will convert 
        #every 60 minutes to 1 hour
        while self.minuteAmount > 60:
            self.minuteAmount -= 60
            self.hourAmount += 1

        #Checks for activity and calulate calories lost based on activity
        if self.fitActivty == "Walking":
            self.avgWalkSpeed = 3.5
            self.weightInKG = self.weight * 0.45359237
            self.walkCalories = ((self.avgWalkSpeed * self.weightInKG * 3.5) / 200)
            self.walkCaloriesTimed = (((self.hourAmount * 60) + self.minuteAmount) * self.walkCalories)
            
            #Shows the user how much calories they burned from walking
            self.activityLabel = Label(self.frameFit, text = "From Walking, you have burned").pack()
            self.answerLabel = Label(self.frameFit ,text = round(self.walkCaloriesTimed)).pack()
            self.calLabel = Label(self.frameFit, text = "Calories").pack()        



class MainWindow:
    #Creates the frame for the main window
    def __init__(self, master):
        mainFrame = Frame(master)
        mainFrame.pack()

        self.titleLabel = Label(master, text = "Calorie Measure")
        self.titleLabel.pack()

        self.caloreBtn = Button(master, text = "Record Fitness Activity", command = self.recordActivty)
        self.caloreBtn.pack()

    #If the button is pressed, it will open a new window
    def recordActivty(self):
        self.record = RecordingFitnessActivity()
        self.record.win.mainloop()


#Starts the main window
winStart = MainWindow(root)
root.mainloop()