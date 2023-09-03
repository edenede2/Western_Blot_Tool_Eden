# Import required libraries
import streamlit as st
import numpy as np
import pandas as pd

# App title
st.title('Western Blot Guidebook :brain: :mouse: \n Gal's Lab')

# Sidebar menu
st.sidebar.title('Navigation')
menu = ['Home', 'Introduction', 'Protocol', 'Calculators']
choice = st.sidebar.selectbox('Choose a section:', menu)

# Home
if choice == 'Home':
    st.subheader('Welcome to the Western Blot Guidebook')
    st.write('This app serves as a comprehensive guide for conducting Western Blots.')

# Introduction
elif choice == 'Introduction':
    st.subheader('Introduction to Western Blot')
    st.write("""
    Here you'll find basic information about what Western Blot is, 
    its applications, and its relevance in neuropsychological research.
    """)

# Steps
elif choice == 'Protocol':
    st.subheader('Step-by-Step Guide')
    steps = ['Sample Preparation', 'Gel Electrophoresis', 'Transfer', 'Blocking', 'Praime Antibody Incubation', 'Secondery Antibody Incubation', 'Detection']
    step_choice = st.selectbox('Choose a step:', steps)
    
    if step_choice == 'Sample Preparation':
        st.write('Detailed information on how to prepare your samples.')
    # Add more steps here...

# Calculators
elif choice == 'Calculators':
    st.subheader('Calculators')
    calculator_types = ['Bradford analysis','Molarity', 'Dilution', 'Volume']
    calculator_choice = st.selectbox('Choose a calculator:', calculator_types)
    
    if calculator_choice == 'Molarity':
        st.write('Molarity calculator will go here.')
    # Add more calculators here...
