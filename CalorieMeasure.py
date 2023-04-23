import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

#Imports code from a Python file named CaloriesBurned
import CaloriesBurned

#Creates the window for Record Fitness Activity
class recordFitnessActivity:

    def __init__(self, master):
        #Creates the frame for the window
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        #Places an image in the window
        #self.fitnessImage = ImageTk.PhotoImage(Image.open("Fitness_Icon.png"))
        #self.labelIcon = tk.Label(self.master, image = self.fitnessImage).pack()

        #Label title of the window
        self.fitActivityLabel = tk.Label(self.master, text = "Record Fitness Activity")
        self.fitActivityLabel.pack()

        #Lets the user choose between four activities
        self.fitnessActivities = ["Walking", "Jogging", "Cycling", "Swimming"]
        self.activityCombo = ttk.Combobox(self.master, value = self.fitnessActivities)
        self.activityCombo.current(0)
        self.activityCombo.bind("<<ComboboxSelected>>")
        self.activityCombo.pack()

        #Asks the user for the amount of hours they spent in an activity
        tk.Label(self.master, text = "Enter the amount of Hours here:").pack()
        self.hourTxt = tk.Entry(self.master, width = 5)
        self.hourTxt.pack()

        #Asks the user for the amount of minutes they spent in an activity
        tk.Label(self.master, text = "Enter the amount of Minutes here:").pack()
        self.minuteTxt = tk.Entry(self.master, width = 5)
        self.minuteTxt.pack()

        #Asks the user for their weight in pounds
        tk.Label(self.master, text = "Enter in your weight in Pounds (lb):").pack()
        self.userWeightTxt = tk.Entry(self.master, width = 5)
        self.userWeightTxt.pack()

        #A button that starts the estimateBurnedCals method
        self.recordBtn = tk.Button(self.master, text = "Record Activity", command = self.estimateBurnedCals)
        self.recordBtn.pack()


    #This method calculates the amount of calories the user have burned
    #based on the activity they chose
    def estimateBurnedCals(self):
        
        #Gets the activity's name
        self.fitActivity = self.activityCombo.get()

        #Validates the user's input and stores the variables in the method
        try:
            self.hourAmount = int(self.hourTxt.get())
            self.minuteAmount = int(self.minuteTxt.get())
            self.userWeight = float(self.userWeightTxt.get())
            pass
        
        #Tells the user that their input is invalid
        except:
            messagebox.showerror("Invaid Input", "Please use numbers when entering information.")

        #Displays the amount of calories they had burned
        self.calAmount = CaloriesBurned.burnedFromActivity(self.fitActivity, self.hourAmount, self.minuteAmount, self.userWeight)
        self.showEstimate = "You have burned an estimated " + str(self.calAmount) + " calories from " + self.fitActivity + "."
        messagebox.showinfo("Calories Burned", self.showEstimate)

    
#Creates the window for Record Calories from Food 
class recordFoodIntake:
    
    def __init__ (self, master):
        #Creates the frame for the window
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        #Places an image in the window
        #self.foodImage = ImageTk.PhotoImage(Image.open("fast-food.png"))
        #self.labelIcon = tk.Label(self.master, image = self.foodImage).pack()

        #Label title for window
        self.foodTitleLabel = tk.Label(self.master, text = "Record Calories from Food")
        self.foodTitleLabel.pack()

        #Asks the user for the food's name they have eaten
        self.foodLable = tk.Label(self.master, text = "Enter the food's name that you ate here:").pack()
        self.foodNameTxt = tk.Entry(self.master, width = 10)
        self.foodNameTxt.pack()

        #Asks the user for the amount of Calories the food contains 
        self.calorieFromFood = tk.Label(self.master, text = "Enter the amount of calories that is contained in the food:").pack()
        self.foodCalTxt = tk.Entry(self.master, width = 10)
        self.foodCalTxt.pack()

        #A button that starts the CalorieFromFood method
        self.recordFoodBtn = tk.Button(self.master, text = "Record Food and Calorie", command = self.CalorieFromFood)
        self.recordFoodBtn.pack()

    #The CalorieFromFood method shows the user the infromation they
    #have entered
    def CalorieFromFood(self):

        #Stores the name of the food in the method's variable
        self.nameOfFood = str(self.foodNameTxt.get())

        #Validates the user's input and stores the variable in the method
        try:
            self.amountOfCalories = float(self.foodCalTxt.get())
            pass
        except:
            messagebox.showerror("Invaid Input", "Please use numbers when entering the amount of calories of the food.")

        #Displays the food's name and amount of calories it has to the user
        self.foodAndCalorie = "You have gained " + str(round(self.amountOfCalories, 2)) + " Calories from eating " + self.nameOfFood + "."
        messagebox.showinfo("Calories from Food", self.foodAndCalorie)


#The main menu of Caloire Measure
class MainNav:

    def __init__(self, master):
        #Creates the frame for the main window
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        #Label title for the main window
        self.titleLable = tk.Label(self.master, text = "Calorie Measure")
        self.titleLable.pack()

        #A button that starts the loadRecordActivity method
        self.calorieBurnedBtn = tk.Button(self.master, text = "Record Fitness Activity", command = self.loadRecordActivity)
        self.calorieBurnedBtn.pack()

        #A button that starts the loadFoodIntake method
        self.calorieIntakeBtn = tk.Button(self.master, text = "Record Calories from Food", command = self.loadFoodIntake)
        self.calorieIntakeBtn.pack()

        #A button that closes the program
        self.stopMainNavBtn = tk.Button(self.master, text = "Exit Program", command = root.quit)
        self.stopMainNavBtn.pack()

    #Contians the elements for the Record Fitness Activity Window
    #and starts the recordFitnessActivity class
    def loadRecordActivity(self):
        self.activityWindow = tk.Toplevel(self.master)
        self.activityWindow.geometry("500x300")
        self.activityWindow.title('Record Fitness Activity')
        self.activityWindow['background'] = '#5c85d6'
        self.app = recordFitnessActivity(self.activityWindow)

    #Contians the elements for the Record Calories from Food Window
    #and starts the recordFoodIntake class
    def loadFoodIntake(self):
        self.foodWindow = tk.Toplevel(self.master)
        self.foodWindow.geometry("500x300")
        self.foodWindow.title('Record Calories from Food')
        self.foodWindow['background'] = '#5c85d6'
        self.app = recordFoodIntake(self.foodWindow)



#Contians the title and size of the window
root = tk.Tk()
root.geometry("600x600")
root.title('Calorie Measure')
root['background'] = '#5c85d6'
#Starts the main window of Calorie Measure
app = MainNav(root)
root.mainloop()