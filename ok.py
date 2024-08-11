import streamlit as st

# Define pickup lines
pickup_lines = {
    'girl': [
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Do you have a map? Because I keep getting lost in your eyes.",
        "If you were a vegetable, you'd be a cute-cumber."
    ],
    'boy': [
        "Do you have a name, or can I call you mine?",
        "Are you a parking ticket? Because you've got 'FINE' written all over you.",
        "If you were a fruit, you'd be a fineapple."
    ]
}

def suggest_pickup_line(gender, keyword):
    # Filter pickup lines by gender and keyword
    filtered_lines = [line for line in pickup_lines[gender] if keyword.lower() in line.lower()]
    
    # If no line matches the keyword, return a random one
    if not filtered_lines:
        return pickup_lines[gender][0]
    
    # Return a random pickup line from the filtered list
    import random
    return random.choice(filtered_lines)

# Streamlit app
st.title("Pickup Line Generator")

# Get user input
gender = st.radio("Select gender", ["Girl", "Boy"]).lower()
keyword = st.text_input("Enter a keyword")

if st.button("Get Pickup Line"):
    if not keyword:
        st.error("Please enter a keyword.")
    else:
        line = suggest_pickup_line(gender, keyword)
        st.write(f"Here's a pickup line for you: **{line}**")
