import streamlit as st
import os
import re

def main():
    # Set page title and configure page layout
    st.set_page_config(page_title="Forecast", page_icon=":chart_with_upwards_trend:")
    
    # Header with custom styling for text color
    st.markdown("<h1 style='color: #123C69;'>Forecast</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("<h3 style='color: blue;'>Welcome to the Forecast dashboard! Here, you can explore our visualizations.</h3>", unsafe_allow_html=True)

    # Define chart names with different colors
    chart_names = [
        "Actual Demand vs Predicted Demand (1)",
        "Actual Demand vs Predicted Demand (2)",
        "Top 10 Customer Sectors by Count",
        "Top 10 Suppliers by Total Revenue",
        "Total Revenue by Sales Channel",
        "Item Quantity Distribution",
        "Profit Distribution",
        "CLV Distribution"
    ]

    # Dropdown menu to select chart
    selected_chart_name = st.selectbox("Select a chart", chart_names)

    # Extract the chart name without HTML tags
    chart_name = re.sub(r"<[^>]*>", "", selected_chart_name)

    # Format the chart name to match file naming convention
    chart_name = f"{chart_name}.png"

    # Construct the full path to the chart image
    chart_path = os.path.join(r"C:/Users/user2022/Desktop/The way to success/charts1", chart_name)

    # Display the selected chart
    st.markdown("---")
    st.markdown(selected_chart_name, unsafe_allow_html=True)
    st.image(chart_path, use_column_width=True, output_format="PNG", caption="Chart Image")

if __name__ == "__main__":
    main()
