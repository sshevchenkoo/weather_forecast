import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")


if place:
    try:
        filter_data = get_data(place, days)
        if options == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filter_data]
            temp = [i/10 for i in temperatures]
            dates = [dict["dt_txt"] for dict in filter_data]
            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if options == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filter_data]
            images_path = [images[conditions] for conditions in sky_conditions]
            st.image(images_path, width=115)
    except KeyError:
        st.write("That place does not exist.")