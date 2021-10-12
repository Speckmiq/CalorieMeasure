#This method calculates an estimated amount of calories the user
#have burned based on an activity
def burnedFromActivity(fitActivity, hourAmount, minuteAmount, userWeight):

    #Stores the variables in the method
    activityName = fitActivity
    amountInHours = hourAmount
    amountInMinutes = minuteAmount
    weightInKG = userWeight * 0.45359237

    #Creates a variable for the method
    caloriesBurned = 0
    

    #Calculates the amount of calories burned based on activity
    if activityName == "Walking":
        avgWalkMET = 3.5
        walkCalories = ((avgWalkMET * weightInKG * 3.5) / 200)
        walkCaloriesTimed = (((amountInHours * 60) + amountInMinutes) * walkCalories)

        #Rounds and store the amount of calories burned into caloriesBurned
        caloriesBurned = round(walkCaloriesTimed, 2)

    elif activityName == "Jogging":
        avgJogMET = 7
        jogCalories = ((avgJogMET * weightInKG * 3.5) / 200)
        jogCaloriesTimed = (((amountInHours * 60) + amountInMinutes) * jogCalories)

        #Rounds and store the amount of calories burned into caloriesBurned
        caloriesBurned = round(jogCaloriesTimed, 2)

    elif activityName == "Cycling":
        avgCycleMET = 8
        cycleCalories = ((avgCycleMET * weightInKG * 3.5) / 200)
        cycleCaloriesTimed = (((amountInHours * 60) + amountInMinutes) * cycleCalories)

        #Rounds and store the amount of calories burned into caloriesBurned
        caloriesBurned = round(cycleCaloriesTimed, 2)

    else:
        avgSwimmingMET = 6
        swimmingCalories = ((avgSwimmingMET * weightInKG * 3.5) / 200)
        swimmingCaloriesTimed = (((amountInHours * 60) + amountInMinutes) * swimmingCalories)

        #Rounds and store the amount of calories burned into caloriesBurned
        caloriesBurned = round(swimmingCaloriesTimed, 2)


    #Returns the amount of calories burned back to the main program
    return caloriesBurned
