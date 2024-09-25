import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Custom styling
st.set_page_config(page_title="BMI Calculator", page_icon="📊", layout="centered")

# Add CSS for styling the background, fonts, and elements
st.markdown("""
    <style>
    /* Background styling */
    .stApp {
        background-color: #f0f2f6;
        background-image: radial-gradient(circle at top left, #a8edea, #fed6e3);
        color: #3E3E3E;
    }
    
    /* Title styling */
    h1 {
        font-family: 'Verdana', sans-serif;
        color: #61c6ce;
    }
    
    /* Subtitle styling */
    h2, h3, h4 {
        font-family: 'Helvetica', sans-serif;
        color: #c17446;
    }
    
    /* Custom font for inputs */
    input {
        font-family: 'Arial', sans-serif;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #000000;
        color: white;
        font-size: 16px;
        font-family: 'Helvetica', sans-serif;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    
    .stButton button:hover {
        background-color: #747373;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    return np.round(bmi, 2)

# Function to categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

# Function to plot BMI categories
def plot_bmi_categories(bmi):
    categories = ['Underweight', 'Normal weight', 'Overweight', 'Obesity']
    values = [18.5, 24.9, 29.9, 40]
    category_colors = ['#FFD700', '#32CD32', '#FFA500', '#FF4500']

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.barh(categories, values, color=category_colors, height=0.5)
    ax.axvline(x=bmi, color='blue', linestyle='--', label=f'Your BMI: {bmi}')

    plt.title('BMI Categories', fontsize=14, fontweight='bold')
    plt.xlabel('BMI Value', fontsize=12)
    plt.ylabel('Category', fontsize=12)
    plt.legend()
    st.pyplot(fig)

# Streamlit App
def main():
    st.title('📊 BMI Calculator & Health Stats Visualizer')
    
    st.write("""
    ### Enter your details to calculate your BMI and visualize your health stats:
    """)

    # Input: weight, height, and age
    weight = st.number_input('Enter your weight (in kg)', min_value=1, max_value=300, value=70)
    height = st.number_input('Enter your height (in cm)', min_value=50, max_value=250, value=170)
    age = st.number_input('Enter your age', min_value=1, max_value=120, value=25)

    if st.button('Calculate BMI'):
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        st.success(f'Your BMI is {bmi} ({category})')

        # Visualize BMI categories with a bar chart
        plot_bmi_categories(bmi)

        # Provide health-related recommendations
        st.write("### Health Recommendations")
        if category == 'Underweight':
            st.info("You are underweight. It's recommended to gain some weight by including more nutrients in your diet.")
        elif category == 'Normal weight':
            st.success("You have a healthy weight. Maintain a balanced diet and regular exercise.")
        elif category == 'Overweight':
            st.warning("You are overweight. Consider adopting a healthier lifestyle through exercise and diet control.")
        else:
            st.error("You fall into the obesity category. It is advisable to seek medical guidance for better health management.")

if __name__ == "__main__":
    main()
