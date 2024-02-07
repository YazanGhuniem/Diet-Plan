def calculate_calories(weight, goal_weight, exercise=False, bulk_up=False):
   
    CALORIES_PER_LB_TO_LOSE = 500  
    CALORIES_PER_LB_TO_GAIN = 250  
    CALORIES_PER_LB_TO_MAINTAIN = 0  
    
    if goal_weight < weight:
        protein = weight
        carbs = 225
        if weight < 100 and weight < 150:
            carbs = 250
            goal_calories = 1500
        elif weight > 150 and weight < 200:
            carbs = 250
            goal_calories = 2000
        elif weight > 200 and weight < 250:
            goal_calories = 2500
        else:
            goal_calories = 2000
        
    elif goal_weight > weight:
        protein = goal_weight
        carbs = 300
        if bulk_up:
            goal_calories = (goal_weight * 10) + 500
            carbs = 325
        else:
            goal_calories = (goal_weight * 10) + 250
    else:
        goal_calories = (goal_weight * 10) + 250
    
    if exercise:
        goal_calories += 250  
    return goal_calories, protein, carbs

def recommend_macros(weight, goal_weight, exercise=False, bulk_up=False):
    
    PROTEIN_RATIO = 0.3  
    CARBS_RATIO = 0.4    
    FAT_RATIO = 0.3      

    total_calories, protein, carbs = calculate_calories(weight, goal_weight, exercise, bulk_up)
    
    protein = total_calories * PROTEIN_RATIO / 4
    carbs = total_calories * CARBS_RATIO / 4
    fats = total_calories * FAT_RATIO / 9

    return protein, carbs, fats

def main():
    weight = float(input("Enter your current weight (in pounds): "))
    goal_weight = float(input("Enter your goal weight (in pounds): "))
    exercise = input("Do you exercise regularly? (yes/no): ").lower()

    if exercise == "yes":
        exercise = True
    else:
        exercise = False

    bulk_up_option = input("Do you want to bulk up? (yes/no): ").lower()
    if bulk_up_option == "yes":
        bulk_up = True
    else:
        bulk_up = False

    required_calories, protein, carbs = calculate_calories(weight, goal_weight, exercise, bulk_up)
    print("Your required daily caloric intake:", required_calories,"calories!")
    print("You should be eating roughly", protein,"grams of protein!")
    print("You should be consuming roughly", carbs,"grams of carbohydrates!")

    protein, carbs, fats = recommend_macros(weight, goal_weight, exercise, bulk_up)
    print("Recommended daily macros:")
    print("Protein: {:.2f} grams".format(protein))
    print("Carbohydrates: {:.2f} grams".format(carbs))
    print("Fats: {:.2f} grams".format(fats))

if __name__ == "__main__":
    main()
