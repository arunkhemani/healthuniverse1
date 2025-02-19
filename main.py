import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Display the Nutrify logo at the top of the app
st.image("images/nurtfiy logo.png", width=300)

# Pie chart
def plot_pie_chart(data, labels, title):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)
    return fig

# Calculate totals based on portions
def calculate_totals(selected_data, portions):
    selected_data = selected_data.copy()
    selected_data["Portions"] = portions
    for column in ["Calories", "Fat (g)", "Protein (g)", "Carbs (g)", "Fiber (g)"]:
        selected_data[column] *= selected_data["Portions"]
    return selected_data, selected_data[["Calories", "Fat (g)", "Protein (g)", "Carbs (g)", "Fiber (g)"]].sum()

# Sodexo Data for Bentley Dining Hall
dining_hall_data = {
  "Monday": {
    "Breakfast": pd.DataFrame([
        {"Meal": "Bacon, Egg And Cheese Muffin", "Calories": 350, "Fat (g)": 12, "Protein (g)": 15, "Carbs (g)": 30, "Fiber (g)": 2},
        {"Meal": "Fried Egg O'muffin Sandwich", "Calories": 310, "Fat (g)": 10, "Protein (g)": 13, "Carbs (g)": 28, "Fiber (g)": 2},
        {"Meal": "Scrambled Eggs", "Calories": 190, "Fat (g)": 5, "Protein (g)": 12, "Carbs (g)": 2, "Fiber (g)": 0},
        {"Meal": "Bacon Slices", "Calories": 70, "Fat (g)": 6, "Protein (g)": 5, "Carbs (g)": 1, "Fiber (g)": 0},
        {"Meal": "Fried Tater Tots", "Calories": 250, "Fat (g)": 15, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 2},
        {"Meal": "Buttermilk Pancakes", "Calories": 180, "Fat (g)": 9, "Protein (g)": 4, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "Everything Omelet", "Calories": 290, "Fat (g)": 20, "Protein (g)": 18, "Carbs (g)": 3, "Fiber (g)": 0},
        {"Meal": "Grits", "Calories": 90, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "Oatmeal", "Calories": 110, "Fat (g)": 2, "Protein (g)": 3, "Carbs (g)": 19, "Fiber (g)": 3},
        {"Meal": "Bacon", "Calories": 60, "Fat (g)": 5, "Protein (g)": 4, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Agave Roasted Peaches", "Calories": 20, "Fat (g)": 0, "Protein (g)": 0, "Carbs (g)": 5, "Fiber (g)": 1},
        {"Meal": "Roasted Mexican Potatoes", "Calories": 45, "Fat (g)": 1, "Protein (g)": 1, "Carbs (g)": 10, "Fiber (g)": 1},
        {"Meal": "Mango Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 24, "Fiber (g)": 1},
        {"Meal": "Strawberry Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 23, "Fiber (g)": 1},
        {"Meal": "Pineapple & Honey Smoothie", "Calories": 190, "Fat (g)": 0, "Protein (g)": 2, "Carbs (g)": 45, "Fiber (g)": 2},
        {"Meal": "Mango Pineapple Smoothie", "Calories": 110, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 26, "Fiber (g)": 1},
        {"Meal": "Brown Sugar Cinnamon Mini Scone", "Calories": 200, "Fat (g)": 10, "Protein (g)": 3, "Carbs (g)": 26, "Fiber (g)": 1},
        {"Meal": "Strawberry Shortcake Muffins", "Calories": 130, "Fat (g)": 5, "Protein (g)": 2, "Carbs (g)": 19, "Fiber (g)": 1},
        {"Meal": "Scrambled Tofu", "Calories": 60, "Fat (g)": 2, "Protein (g)": 7, "Carbs (g)": 1, "Fiber (g)": 1},
        {"Meal": "Lyonnaise Potatoes", "Calories": 45, "Fat (g)": 1, "Protein (g)": 1, "Carbs (g)": 10, "Fiber (g)": 1},
        {"Meal": "Roasted Red Beets", "Calories": 25, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 5, "Fiber (g)": 1},
     ]),
    "Lunch": pd.DataFrame([
        {"Meal": "Brown Rice", "Calories": 90, "Fat (g)": 0.5, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "Sauteed Collard Greens", "Calories": 80, "Fat (g)": 5, "Protein (g)": 2, "Carbs (g)": 8, "Fiber (g)": 3},
        {"Meal": "Steamed Broccoli", "Calories": 10, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Roasted Brussels Sprouts", "Calories": 20, "Fat (g)": 1, "Protein (g)": 1, "Carbs (g)": 3, "Fiber (g)": 2},
        {"Meal": "Garlic Orange Chili Tofu", "Calories": 420, "Fat (g)": 20, "Protein (g)": 30, "Carbs (g)": 30, "Fiber (g)": 5},
        {"Meal": "White Rice", "Calories": 190, "Fat (g)": 0.5, "Protein (g)": 3, "Carbs (g)": 40, "Fiber (g)": 1},
        {"Meal": "Grilled Fresh Tilapia", "Calories": 180, "Fat (g)": 5, "Protein (g)": 25, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Crispy Smashed Red Bliss Potato", "Calories": 170, "Fat (g)": 8, "Protein (g)": 2, "Carbs (g)": 25, "Fiber (g)": 2},
        {"Meal": "Balsamic Roasted Vegetables", "Calories": 60, "Fat (g)": 2, "Protein (g)": 2, "Carbs (g)": 10, "Fiber (g)": 3},
        {"Meal": "Bbq Chicken Thigh", "Calories": 190, "Fat (g)": 10, "Protein (g)": 20, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Tomato, Bacon & Cheddar Baguette", "Calories": 540, "Fat (g)": 25, "Protein (g)": 20, "Carbs (g)": 50, "Fiber (g)": 2},
        {"Meal": "Grilled Garlic Chicken", "Calories": 150, "Fat (g)": 2, "Protein (g)": 30, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Black Bean Burger", "Calories": 240, "Fat (g)": 10, "Protein (g)": 12, "Carbs (g)": 28, "Fiber (g)": 5},
        {"Meal": "Cheeseburger On Bun", "Calories": 200, "Fat (g)": 8, "Protein (g)": 15, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "French Fries", "Calories": 150, "Fat (g)": 8, "Protein (g)": 2, "Carbs (g)": 18, "Fiber (g)": 2},
        {"Meal": "Bbq Pork Riblet Sandwich", "Calories": 380, "Fat (g)": 12, "Protein (g)": 25, "Carbs (g)": 45, "Fiber (g)": 3},
        {"Meal": "Beef Bulgogi Rice Bowl", "Calories": 470, "Fat (g)": 20, "Protein (g)": 35, "Carbs (g)": 50, "Fiber (g)": 5},
        {"Meal": "Cheese Pizza", "Calories": 250, "Fat (g)": 8, "Protein (g)": 10, "Carbs (g)": 32, "Fiber (g)": 2},
        {"Meal": "Vegetable Lovers Feast Pizza", "Calories": 290, "Fat (g)": 12, "Protein (g)": 8, "Carbs (g)": 35, "Fiber (g)": 3},
        {"Meal": "Pepperoni Pizza", "Calories": 250, "Fat (g)": 10, "Protein (g)": 10, "Carbs (g)": 32, "Fiber (g)": 2},
      ]),
    "Dinner": pd.DataFrame([
        {"Meal": "Herb Grilled Chicken Breast", "Calories": 160, "Fat (g)": 5, "Protein (g)": 30, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Roasted Brussels Sprouts", "Calories": 20, "Fat (g)": 1, "Protein (g)": 1, "Carbs (g)": 3, "Fiber (g)": 2},
        {"Meal": "Brown Rice", "Calories": 90, "Fat (g)": 0.5, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "White Rice", "Calories": 190, "Fat (g)": 0.5, "Protein (g)": 3, "Carbs (g)": 40, "Fiber (g)": 1},
        {"Meal": "Creole Sauce", "Calories": 35, "Fat (g)": 1, "Protein (g)": 0, "Carbs (g)": 6, "Fiber (g)": 1},
        {"Meal": "Roast Loin Of Pork", "Calories": 210, "Fat (g)": 10, "Protein (g)": 25, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Rice & Red Beans", "Calories": 180, "Fat (g)": 3, "Protein (g)": 5, "Carbs (g)": 35, "Fiber (g)": 4},
        {"Meal": "Sauteed Yellow Squash & Zucchini", "Calories": 90, "Fat (g)": 5, "Protein (g)": 1, "Carbs (g)": 10, "Fiber (g)": 2},
        {"Meal": "Garlic Breadstick", "Calories": 160, "Fat (g)": 5, "Protein (g)": 3, "Carbs (g)": 25, "Fiber (g)": 1},
        {"Meal": "Vegetable Lovers Feast Pizza", "Calories": 290, "Fat (g)": 12, "Protein (g)": 8, "Carbs (g)": 35, "Fiber (g)": 3},
        {"Meal": "Cheese Pizza", "Calories": 250, "Fat (g)": 8, "Protein (g)": 10, "Carbs (g)": 32, "Fiber (g)": 2},
        {"Meal": "Pepperoni Pizza", "Calories": 250, "Fat (g)": 10, "Protein (g)": 10, "Carbs (g)": 32, "Fiber (g)": 2},
    ]),
  },
   "Tuesday": {
    "Breakfast": pd.DataFrame([
        {"Meal": "Egg & Cheese Bagel With Sausage", "Calories": 500, "Fat (g)": 20, "Protein (g)": 22, "Carbs (g)": 55, "Fiber (g)": 3},
        {"Meal": "Scrambled Egg & Cheese On Bagel", "Calories": 300, "Fat (g)": 10, "Protein (g)": 15, "Carbs (g)": 35, "Fiber (g)": 2},
        {"Meal": "Scrambled Eggs", "Calories": 190, "Fat (g)": 5, "Protein (g)": 12, "Carbs (g)": 2, "Fiber (g)": 0},
        {"Meal": "Oven Roasted Greek Potatoes", "Calories": 100, "Fat (g)": 2, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 2},
        {"Meal": "Grilled Kielbasa", "Calories": 190, "Fat (g)": 16, "Protein (g)": 8, "Carbs (g)": 1, "Fiber (g)": 0},
        {"Meal": "French Waffle", "Calories": 180, "Fat (g)": 7, "Protein (g)": 4, "Carbs (g)": 22, "Fiber (g)": 1},
        {"Meal": "Everything Omelet", "Calories": 290, "Fat (g)": 20, "Protein (g)": 18, "Carbs (g)": 3, "Fiber (g)": 0},
        {"Meal": "Grits", "Calories": 90, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "Oatmeal", "Calories": 110, "Fat (g)": 2, "Protein (g)": 3, "Carbs (g)": 19, "Fiber (g)": 3},
        {"Meal": "Griddled Ham Steak", "Calories": 70, "Fat (g)": 3, "Protein (g)": 10, "Carbs (g)": 1, "Fiber (g)": 0},
        {"Meal": "Potato & Kale Hash", "Calories": 130, "Fat (g)": 5, "Protein (g)": 3, "Carbs (g)": 15, "Fiber (g)": 2},
        {"Meal": "Chocolate Strawberry Chia Seed Pudding", "Calories": 290, "Fat (g)": 15, "Protein (g)": 8, "Carbs (g)": 28, "Fiber (g)": 6},
        {"Meal": "Strawberry Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 23, "Fiber (g)": 1},
        {"Meal": "Mango Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 24, "Fiber (g)": 1},
        {"Meal": "Mango Pineapple Smoothie", "Calories": 110, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 26, "Fiber (g)": 1},
        {"Meal": "Fresh Melons, Strawberries & Grapes", "Calories": 25, "Fat (g)": 0, "Protein (g)": 0, "Carbs (g)": 6, "Fiber (g)": 0},
        {"Meal": "Scrambled Vegan Egg Substitute", "Calories": 100, "Fat (g)": 3, "Protein (g)": 8, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Shredded Hash Browns", "Calories": 260, "Fat (g)": 12, "Protein (g)": 3, "Carbs (g)": 30, "Fiber (g)": 2},
        {"Meal": "Roasted Carrots", "Calories": 40, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 10, "Fiber (g)": 3},
    ]),
    "Lunch": pd.DataFrame([
        {"Meal": "Steamed Italian Vegetable Medley", "Calories": 45, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 9, "Fiber (g)": 3},
        {"Meal": "Rosemary Grilled Pork Chop", "Calories": 300, "Fat (g)": 10, "Protein (g)": 30, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Steamed Broccoli", "Calories": 10, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Simply Roasted Cauliflower", "Calories": 30, "Fat (g)": 1, "Protein (g)": 1, "Carbs (g)": 3, "Fiber (g)": 2},
        {"Meal": "Lentils & Swiss Chard", "Calories": 90, "Fat (g)": 2, "Protein (g)": 6, "Carbs (g)": 14, "Fiber (g)": 4},
        {"Meal": "Extra Firm Tofu", "Calories": 30, "Fat (g)": 2, "Protein (g)": 3, "Carbs (g)": 1, "Fiber (g)": 1},
        {"Meal": "Mashed Potatoes", "Calories": 70, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 10, "Fiber (g)": 1},
        {"Meal": "Steamed Green Beans", "Calories": 30, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 7, "Fiber (g)": 2},
        {"Meal": "Jasmine Rice", "Calories": 100, "Fat (g)": 0, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 1},
        {"Meal": "Garlic Rice", "Calories": 160, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 32, "Fiber (g)": 2},
        {"Meal": "Beef Top Round Machaca", "Calories": 140, "Fat (g)": 5, "Protein (g)": 20, "Carbs (g)": 2, "Fiber (g)": 0},
        {"Meal": "Southern Style Green Beans", "Calories": 90, "Fat (g)": 3, "Protein (g)": 3, "Carbs (g)": 10, "Fiber (g)": 2},
        {"Meal": "Chicken Bacon Club Loafer Sandwich", "Calories": 430, "Fat (g)": 20, "Protein (g)": 30, "Carbs (g)": 35, "Fiber (g)": 3},
        {"Meal": "French Fries", "Calories": 150, "Fat (g)": 8, "Protein (g)": 2, "Carbs (g)": 18, "Fiber (g)": 2},
        {"Meal": "Grilled Garlic Chicken", "Calories": 150, "Fat (g)": 2, "Protein (g)": 30, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Black Bean Burger", "Calories": 240, "Fat (g)": 10, "Protein (g)": 12, "Carbs (g)": 28, "Fiber (g)": 5},
        {"Meal": "Italian Turkey And Ham Loafer Sandwich", "Calories": 370, "Fat (g)": 15, "Protein (g)": 25, "Carbs (g)": 35, "Fiber (g)": 2},
        {"Meal": "Cumin Shrimp And Spicy Pinto Bean Bowl", "Calories": 720, "Fat (g)": 25, "Protein (g)": 50, "Carbs (g)": 60, "Fiber (g)": 8},
        {"Meal": "Pepperoni Pizza", "Calories": 250, "Fat (g)": 10, "Protein (g)": 10, "Carbs (g)": 32, "Fiber (g)": 2},
        {"Meal": "Cheese Pizza", "Calories": 250, "Fat (g)": 8, "Protein (g)": 10, "Carbs (g)": 32, "Fiber (g)": 2},
        {"Meal": "Vegetable Lovers Feast Pizza", "Calories": 290, "Fat (g)": 12, "Protein (g)": 8, "Carbs (g)": 35, "Fiber (g)": 3},
        {"Meal": "Green Bean Casserole", "Calories": 80, "Fat (g)": 4, "Protein (g)": 2, "Carbs (g)": 8, "Fiber (g)": 1},
    ]),
    "Dinner": pd.DataFrame([
        {"Meal": "Steamed Italian Vegetable Medley", "Calories": 45, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 9, "Fiber (g)": 3},
        {"Meal": "Mashed Potatoes", "Calories": 70, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 10, "Fiber (g)": 1},
        {"Meal": "Simply Grilled Fresh Cod", "Calories": 150, "Fat (g)": 2, "Protein (g)": 30, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Chive And Garlic Mashed Potatoes", "Calories": 190, "Fat (g)": 8, "Protein (g)": 4, "Carbs (g)": 25, "Fiber (g)": 2},
        {"Meal": "Roasted Brussels Sprouts", "Calories": 20, "Fat (g)": 1, "Protein (g)": 1, "Carbs (g)": 3, "Fiber (g)": 2},
        {"Meal": "Simple Baked Chicken", "Calories": 420, "Fat (g)": 15, "Protein (g)": 35, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Tuna Cheddar Melt", "Calories": 520, "Fat (g)": 20, "Protein (g)": 30, "Carbs (g)": 50, "Fiber (g)": 3},
        {"Meal": "Alfredo Sauce", "Calories": 190, "Fat (g)": 12, "Protein (g)": 2, "Carbs (g)": 10, "Fiber (g)": 1},
        {"Meal": "Cavatappi Pasta", "Calories": 390, "Fat (g)": 8, "Protein (g)": 10, "Carbs (g)": 70, "Fiber (g)": 3},
        {"Meal": "Vegetable Lovers Feast Pizza", "Calories": 290, "Fat (g)": 12, "Protein (g)": 8, "Carbs (g)": 35, "Fiber (g)": 3},
        {"Meal": "Broccoli Cheddar Ranch Pizza", "Calories": 330, "Fat (g)": 15, "Protein (g)": 8, "Carbs (g)": 35, "Fiber (g)": 2},
        {"Meal": "Mexican Brown Rice", "Calories": 180, "Fat (g)": 2, "Protein (g)": 4, "Carbs (g)": 35, "Fiber (g)": 3},
        {"Meal": "Brussels Sprouts & Citrus Salad", "Calories": 60, "Fat (g)": 2, "Protein (g)": 2, "Carbs (g)": 8, "Fiber (g)": 2},
    ]),
},
    "Wednesday": {
    "Breakfast": pd.DataFrame([
        {"Meal": "Ham, Egg And Cheese Taco", "Calories": 220, "Fat (g)": 12, "Protein (g)": 14, "Carbs (g)": 18, "Fiber (g)": 2},
        {"Meal": "Egg And Cheese Breakfast Taco", "Calories": 210, "Fat (g)": 10, "Protein (g)": 12, "Carbs (g)": 17, "Fiber (g)": 2},
        {"Meal": "Blueberry Pancakes", "Calories": 220, "Fat (g)": 7, "Protein (g)": 5, "Carbs (g)": 32, "Fiber (g)": 1},
        {"Meal": "O'Brien Potatoes", "Calories": 140, "Fat (g)": 5, "Protein (g)": 2, "Carbs (g)": 18, "Fiber (g)": 2},
        {"Meal": "Pork Sausage Link", "Calories": 100, "Fat (g)": 8, "Protein (g)": 5, "Carbs (g)": 1, "Fiber (g)": 0},
        {"Meal": "Scrambled Eggs", "Calories": 190, "Fat (g)": 5, "Protein (g)": 12, "Carbs (g)": 2, "Fiber (g)": 0},
        {"Meal": "Everything Omelet", "Calories": 290, "Fat (g)": 20, "Protein (g)": 18, "Carbs (g)": 3, "Fiber (g)": 0},
        {"Meal": "Grits", "Calories": 90, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "Oatmeal", "Calories": 110, "Fat (g)": 2, "Protein (g)": 3, "Carbs (g)": 19, "Fiber (g)": 3},
        {"Meal": "Hash Browned Potatoes", "Calories": 120, "Fat (g)": 6, "Protein (g)": 2, "Carbs (g)": 15, "Fiber (g)": 2},
        {"Meal": "Turkey Sausage Patty", "Calories": 80, "Fat (g)": 6, "Protein (g)": 8, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Sweet Potato Pancakes", "Calories": 270, "Fat (g)": 8, "Protein (g)": 6, "Carbs (g)": 40, "Fiber (g)": 4},
        {"Meal": "Mango Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 24, "Fiber (g)": 1},
        {"Meal": "Mango Pineapple Smoothie", "Calories": 110, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 26, "Fiber (g)": 1},
        {"Meal": "Pineapple & Honey Smoothie", "Calories": 190, "Fat (g)": 0, "Protein (g)": 2, "Carbs (g)": 45, "Fiber (g)": 2},
        {"Meal": "Strawberry Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 23, "Fiber (g)": 1},
        {"Meal": "Sauteed Peppers & Onions", "Calories": 80, "Fat (g)": 5, "Protein (g)": 1, "Carbs (g)": 8, "Fiber (g)": 2},
        {"Meal": "Scrambled Tofu", "Calories": 60, "Fat (g)": 3, "Protein (g)": 6, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Classic Grits", "Calories": 100, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 1},
        ]),
        "Lunch": pd.DataFrame([
        {"Meal": "Balsamic Collard Greens", "Calories": 330, "Fat (g)": 5, "Protein (g)": 6, "Carbs (g)": 20, "Fiber (g)": 8},
        {"Meal": "Turkish Bulgur Pilaf With Garbanzo Beans", "Calories": 510, "Fat (g)": 8, "Protein (g)": 18, "Carbs (g)": 80, "Fiber (g)": 12},
        {"Meal": "Grilled Steak", "Calories": 260, "Fat (g)": 15, "Protein (g)": 25, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Jasmine Rice", "Calories": 100, "Fat (g)": 0, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 0},
        {"Meal": "Simply Smashed Yukon Gold Potatoes", "Calories": 110, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 2},
        {"Meal": "Caribbean Style Ratatouille", "Calories": 80, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 12, "Fiber (g)": 3},
        {"Meal": "Steamed Broccoli", "Calories": 10, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Sticky Rice", "Calories": 210, "Fat (g)": 0, "Protein (g)": 3, "Carbs (g)": 46, "Fiber (g)": 1},
        {"Meal": "Warm Pita Bread", "Calories": 190, "Fat (g)": 4, "Protein (g)": 6, "Carbs (g)": 34, "Fiber (g)": 2},
        {"Meal": "Pork Souvlaki Bowl", "Calories": 580, "Fat (g)": 22, "Protein (g)": 40, "Carbs (g)": 48, "Fiber (g)": 4},
        {"Meal": "Greek Salad", "Calories": 20, "Fat (g)": 1, "Protein (g)": 1, "Carbs (g)": 3, "Fiber (g)": 1},
        {"Meal": "Tomato, Mozzarella & Pesto Panini", "Calories": 550, "Fat (g)": 25, "Protein (g)": 20, "Carbs (g)": 60, "Fiber (g)": 4},
        {"Meal": "Cheeseburger On Bun", "Calories": 200, "Fat (g)": 8, "Protein (g)": 12, "Carbs (g)": 25, "Fiber (g)": 1},
        {"Meal": "French Fries", "Calories": 150, "Fat (g)": 5, "Protein (g)": 2, "Carbs (g)": 24, "Fiber (g)": 2},
        {"Meal": "Grilled Garlic Chicken", "Calories": 150, "Fat (g)": 2, "Protein (g)": 30, "Carbs (g)": 0, "Fiber (g)": 0},
        ]),
        "Dinner": pd.DataFrame([
        {"Meal": "Steamed Broccoli", "Calories": 10, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Sticky Rice", "Calories": 160, "Fat (g)": 0, "Protein (g)": 3, "Carbs (g)": 37, "Fiber (g)": 1},
        {"Meal": "Herb Roast Chicken Breast", "Calories": 130, "Fat (g)": 3, "Protein (g)": 25, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Turkish Bulgur Pilaf With Garbanzo Beans", "Calories": 510, "Fat (g)": 8, "Protein (g)": 18, "Carbs (g)": 80, "Fiber (g)": 12},
        {"Meal": "Simply Smashed Yukon Gold Potatoes", "Calories": 110, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 2},
        {"Meal": "Jasmine Rice", "Calories": 100, "Fat (g)": 0, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 0},
        {"Meal": "Balsamic Collard Greens", "Calories": 330, "Fat (g)": 5, "Protein (g)": 6, "Carbs (g)": 20, "Fiber (g)": 8},
        {"Meal": "Caribbean Style Ratatouille", "Calories": 80, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 12, "Fiber (g)": 3},
        {"Meal": "Curly Fries", "Calories": 290, "Fat (g)": 15, "Protein (g)": 4, "Carbs (g)": 35, "Fiber (g)": 3},
        {"Meal": "Chicken Nuggets", "Calories": 350, "Fat (g)": 20, "Protein (g)": 15, "Carbs (g)": 22, "Fiber (g)": 2},
        {"Meal": "Baked Macaroni & Cheese", "Calories": 180, "Fat (g)": 10, "Protein (g)": 6, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "Tomato, Mozzarella & Pesto Panini", "Calories": 550, "Fat (g)": 25, "Protein (g)": 20, "Carbs (g)": 60, "Fiber (g)": 4},
        ]),
      },

  "Thursday": {
    "Breakfast": pd.DataFrame([
        {"Meal": "Fried Egg O'muffin", "Calories": 270, "Fat (g)": 10, "Protein (g)": 12, "Carbs (g)": 30, "Fiber (g)": 1},
        {"Meal": "Fried Egg O'muffin With Bacon", "Calories": 310, "Fat (g)": 15, "Protein (g)": 15, "Carbs (g)": 28, "Fiber (g)": 1},
        {"Meal": "Vanilla Belgian Waffle", "Calories": 260, "Fat (g)": 9, "Protein (g)": 6, "Carbs (g)": 32, "Fiber (g)": 1},
        {"Meal": "Scrambled Eggs", "Calories": 190, "Fat (g)": 5, "Protein (g)": 12, "Carbs (g)": 2, "Fiber (g)": 0},
        {"Meal": "Lyonnaise Potatoes", "Calories": 90, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 15, "Fiber (g)": 2},
        {"Meal": "Canadian Bacon", "Calories": 60, "Fat (g)": 2, "Protein (g)": 7, "Carbs (g)": 1, "Fiber (g)": 0},
        {"Meal": "Everything Omelet", "Calories": 290, "Fat (g)": 20, "Protein (g)": 18, "Carbs (g)": 3, "Fiber (g)": 0},
        {"Meal": "Grits", "Calories": 90, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 20, "Fiber (g)": 1},
        {"Meal": "Oatmeal", "Calories": 110, "Fat (g)": 2, "Protein (g)": 3, "Carbs (g)": 19, "Fiber (g)": 3},
        {"Meal": "Fruit Salad", "Calories": 35, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 8, "Fiber (g)": 2},
        {"Meal": "Southwest Sausage Breakfast Bowl", "Calories": 390, "Fat (g)": 25, "Protein (g)": 20, "Carbs (g)": 25, "Fiber (g)": 4},
        {"Meal": "Roasted Red Bliss Potatoes", "Calories": 120, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 2},
        {"Meal": "Mango Pineapple Smoothie", "Calories": 110, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 26, "Fiber (g)": 1},
        {"Meal": "Mango Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 24, "Fiber (g)": 1},
        {"Meal": "Strawberry Banana Smoothie", "Calories": 100, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 23, "Fiber (g)": 1},
        {"Meal": "Pineapple & Honey Smoothie", "Calories": 190, "Fat (g)": 0, "Protein (g)": 2, "Carbs (g)": 45, "Fiber (g)": 2},
        {"Meal": "S'mores Scone", "Calories": 340, "Fat (g)": 15, "Protein (g)": 5, "Carbs (g)": 45, "Fiber (g)": 1},
        {"Meal": "Corn Muffin", "Calories": 170, "Fat (g)": 6, "Protein (g)": 3, "Carbs (g)": 23, "Fiber (g)": 1},
        {"Meal": "Steamed Cauliflower", "Calories": 15, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 3, "Fiber (g)": 1},
        {"Meal": "Hash Brown Patty", "Calories": 150, "Fat (g)": 8, "Protein (g)": 2, "Carbs (g)": 18, "Fiber (g)": 2},
        {"Meal": "Scrambled Vegan Egg Substitute", "Calories": 100, "Fat (g)": 3, "Protein (g)": 8, "Carbs (g)": 2, "Fiber (g)": 1},
    ]),
    "Lunch": pd.DataFrame([
        {"Meal": "Steamed Broccoli", "Calories": 10, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Jasmine Rice", "Calories": 100, "Fat (g)": 0.5, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 1},
        {"Meal": "Fresh Spinach", "Calories": 0, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 1, "Fiber (g)": 1},
        {"Meal": "Oven Roast Garlic Red Potatoes", "Calories": 130, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 25, "Fiber (g)": 2},
        {"Meal": "Cajun Turkey Breast", "Calories": 90, "Fat (g)": 2, "Protein (g)": 20, "Carbs (g)": 0, "Fiber (g)": 0},
        {"Meal": "Extra Firm Tofu", "Calories": 60, "Fat (g)": 2, "Protein (g)": 5, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Cuban Black Beans And Rice", "Calories": 170, "Fat (g)": 3, "Protein (g)": 7, "Carbs (g)": 30, "Fiber (g)": 5},
        {"Meal": "Plain Cooked Farro", "Calories": 60, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 11, "Fiber (g)": 2},
    ]),
    "Dinner": pd.DataFrame([
        {"Meal": "Steamed Broccoli", "Calories": 10, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 2, "Fiber (g)": 1},
        {"Meal": "Fresh Spinach", "Calories": 0, "Fat (g)": 0, "Protein (g)": 1, "Carbs (g)": 1, "Fiber (g)": 1},
        {"Meal": "Cuban Black Beans And Rice", "Calories": 170, "Fat (g)": 3, "Protein (g)": 7, "Carbs (g)": 30, "Fiber (g)": 5},
        {"Meal": "Plain Cooked Farro", "Calories": 60, "Fat (g)": 1, "Protein (g)": 2, "Carbs (g)": 11, "Fiber (g)": 2},
        {"Meal": "Jasmine Rice", "Calories": 100, "Fat (g)": 0.5, "Protein (g)": 2, "Carbs (g)": 22, "Fiber (g)": 1},
        {"Meal": "Oven Roast Garlic Red Potatoes", "Calories": 130, "Fat (g)": 3, "Protein (g)": 2, "Carbs (g)": 25, "Fiber (g)": 2},
        {"Meal": "Grilled Jerk Chicken Breast", "Calories": 150, "Fat (g)": 5, "Protein (g)": 30, "Carbs (g)": 0, "Fiber (g)": 0},
    ]),
  },
}
        
# Sidebar for user personal info
st.sidebar.header("Personal Information")
weight = st.sidebar.number_input("Weight (kg):", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (cm):", min_value=100, max_value=250, value=170)
age = st.sidebar.number_input("Age (years):", min_value=10, max_value=100, value=25)
gender = st.sidebar.selectbox("Gender:", ["Male", "Female", "Other"])
activity_level = st.sidebar.selectbox("Activity Level:", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

# Calculate daily caloric needs
if gender == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

activity_multiplier = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
}
daily_caloric_needs = int(bmr * activity_multiplier[activity_level])
st.sidebar.metric("Recommended Daily Calories", f"{daily_caloric_needs} kcal")

# Sidebar for day and meal type selection
st.sidebar.header("Select Day and Meal Type")
selected_day = st.sidebar.selectbox("Select a Day:", list(dining_hall_data.keys()))
selected_meal_type = st.sidebar.selectbox("Select a Meal Type:", ["Breakfast", "Lunch", "Dinner"])

# Retrieve menu for selected day and meal type
menu_df = dining_hall_data[selected_day][selected_meal_type]
st.subheader(f"{selected_day} {selected_meal_type} Menu")
st.dataframe(menu_df)

# Allow users to select meals and portions
selected_meals = st.multiselect(
    "Select meals to add to your plan:",
    options=menu_df["Meal"].tolist()
)

# After meals are selected and totals are calculated
if selected_meals:
    selected_data = menu_df[menu_df["Meal"].isin(selected_meals)]
    st.write("### Selected Meals")

    # Input portions for selected meals
    portions = []
    for meal in selected_meals:
        portions.append(st.number_input(f"Portions of {meal}:", min_value=1, max_value=10, value=1))

    # Calculate totals
    selected_data, totals = calculate_totals(selected_data, portions)

    # Display selected meals with portions
    st.table(selected_data)

    # Display summary
    st.write("### Summary")
    st.metric("Total Calories", f"{totals['Calories']} kcal")
    st.metric("Fat", f"{totals['Fat (g)']} g")
    st.metric("Total Protein", f"{totals['Protein (g)']} g")
    st.metric("Total Carbs", f"{totals['Carbs (g)']} g")
    st.metric("Total Fiber", f"{totals['Fiber (g)']} g")

    # Nutritional Breakdown Pie Chart
    st.subheader("Nutritional Breakdown")
    pie_chart = plot_pie_chart(
        data=[totals["Carbs (g)"], totals["Protein (g)"], totals["Fat (g)"]],
        labels=["Carbs (g)", "Protein (g)", "Fat (g)"],
        title="Nutritional Distribution"
    )
    st.pyplot(pie_chart)

    # Recommendations Section
    recommendations = []

    # Macronutrient Needs Calculations
    protein_grams_needed = round(weight * 1.0)
    fat_calories_needed = daily_caloric_needs * 0.25
    fat_grams_needed = round(fat_calories_needed / 9)
    protein_calories_needed = protein_grams_needed * 4
    carbs_calories_needed = daily_caloric_needs - (protein_calories_needed + fat_calories_needed)
    carbs_grams_needed = round(carbs_calories_needed / 4)

    # Generate recommendations based on totals
    if totals["Protein (g)"] < protein_grams_needed / 3:
        recommendations.append(
            f"Your meal is still too low in protein ({totals['Protein (g)']} g). You need approximately round({protein_grams_needed / 3}) g. "
            "Consider adding options like 'Grilled Garlic Chicken', 'Black Bean Burger', or 'Scrambled Eggs'."
        )
    else:
        st.success("Your meal plan meets your protein needs!")
        
    if totals["Carbs (g)"] < carbs_grams_needed / 3 :
        recommendations.append(
            f"Your meal is still low in carbohydrates ({totals['Carbs (g)']} g). You need approximately round({carbs_grams_needed / 3}) g. "
            "Consider adding options like 'Jasmine Rice', 'Oatmeal', or 'Brown Rice'."
        )
    else:
        st.success("Your meal plan meets your carbohydrates needs!")
        
    if totals["Fat (g)"] < fat_grams_needed / 3 :
        recommendations.append(
            f"Your meal is still low in fats ({totals['Fat (g)']} g). You need approximately round({fat_grams_needed / 3}) g. "
            "Consider adding options like 'Bacon Slices', 'Scrambled Tofu', or 'Avocado'."
        )
    else:
        st.success("Your meal meets your fat needs! ")
         
    # Display Recommendations
    if recommendations:
        st.subheader("Recommendations for a Balanced Meal")
        for recommendation in recommendations:
            st.warning(recommendation)
    else:
        st.success("Your meal plan meets all your macronutrient needs. Great job!")

    # Dietitian Section
    st.markdown("---")
    st.header("Need Help with Your Diet?")
    st.write("If you have questions or concerns about your diet, you can book an appointment with our on-site campus dietitian.")
    
    # Display dietitian information
    st.image("images/Hayley_tcm17-45509.jpg", caption="Hayley Ruff RD, LDN", width=300)
    st.write("**Dietitian: Hayley Ruff RD, LDN**")
    st.write("📧 **Email:** [hayley.ruff@sodexo.com](mailto:hayley.ruff@sodexo.com)")
    st.write("📞 **Phone:** +1 (508) 414-9633")
    
    # Appointment Booking Form
    st.subheader("Book an Appointment")
    with st.form("dietitian_appointment_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("What would you like to discuss?")
        submitted = st.form_submit_button("Submit Appointment Request")
    
        if submitted:
            st.success(f"Thank you, {name}! Your request has been submitted. Hayley Ruff will reach out to you at {email} soon.")
