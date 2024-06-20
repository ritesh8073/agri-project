def get_crop_nutrient_requirements(crop):
    
    crop_nutrient_requirements = {
        "Wheat": {"N": (20, 40), "P": (30, 50), "K": (20, 40)},
        "Rice": {"N": (30, 50), "P": (20, 40), "K": (30, 50)},
        "Corn": {"N": (40, 60), "P": (30, 50), "K": (20, 40)},
        "Barley": {"N": (10, 30), "P": (20, 40), "K": (10, 30)},
        "Soybean": {"N": (20, 40), "P": (20, 40), "K": (30, 50)},
        "Oat": {"N": (15, 30), "P": (20, 40), "K": (15, 30)},
        "Peanut": {"N": (20, 40), "P": (30, 50), "K": (30, 50)},
        "Sugarcane": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Tomato": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Potato": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Carrot": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Onion": {"N": (20, 40), "P": (30, 50), "K": (20, 40)},
        "Garlic": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Peas": {"N": (10, 30), "P": (20, 40), "K": (20, 40)},
        "Beans": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Lettuce": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Spinach": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Cabbage": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Broccoli": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Cauliflower": {"N": (20, 40), "P": (20, 40), "K": (20, 40)},
        "Cucumber": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Pumpkin": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Squash": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Zucchini": {"N": (30, 50), "P": (30, 50), "K": (30, 50)},
        "Apple": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Banana": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Orange": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Grape": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Mango": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Pineapple": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Papaya": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        "Strawberry": {"N": (50, 100), "P": (40, 80), "K": (50, 100)},
        # Add more crops with their optimal ranges here
    }
    return crop_nutrient_requirements.get(crop, None)

def suggest_fertilizer(nitrogen, phosphorus, potassium, crop):
    crop_requirements = get_crop_nutrient_requirements(crop)
    
    if not crop_requirements:
        return f"No nutrient requirements found for {crop}. Please add the crop's nutrient requirements."
    
    suggestions = []

    
    if nitrogen < crop_requirements["N"][0]:
        suggestions.append("Add nitrogen-rich fertilizer.")
    elif nitrogen > crop_requirements["N"][1]:
        suggestions.append("Reduce nitrogen application.")

    if phosphorus < crop_requirements["P"][0]:
        suggestions.append("Add phosphorus-rich fertilizer.")
    elif phosphorus > crop_requirements["P"][1]:
        suggestions.append("Reduce phosphorus application.")

    if potassium < crop_requirements["K"][0]:
        suggestions.append("Add potassium-rich fertilizer.")
    elif potassium > crop_requirements["K"][1]:
        suggestions.append("Reduce potassium application.")

    if not suggestions:
        return "Your soil has optimal nutrient levels for the selected crop."
    else:
        return " ".join(suggestions)

def main():
    crop = input("Enter the crop you want to grow: ")
    nitrogen = float(input("Enter the nitrogen content of your soil (N): "))
    phosphorus = float(input("Enter the phosphorus content of your soil (P): "))
    potassium = float(input("Enter the potassium content of your soil (K): "))

    recommendation = suggest_fertilizer(nitrogen, phosphorus, potassium, crop)
    print(recommendation)

if __name__ == "__main__":
    main()
