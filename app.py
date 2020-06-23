import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
import streamlit as st
import pickle

model = pickle.load(open('house_price_prediction.pkl','rb'))
house_data7 = pd.read_csv('house_df7.csv')

def house_price_prediction(location, sqft, bhk, bath):
    location_index = np.where(house_data7.drop(['price'], axis=1).columns==location)[0][0]
    x = np.zeros(len(house_data7.drop(['price'], axis=1).columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location_index >= 0:
        x[location_index] = 1
    price = int(round(model.predict([x])[0] * 100000))
    return price

def menuCategory():
    menu = ['EDA','Plot','Prediction']
    choice = st.sidebar.selectbox("Select Category", menu)
    house_data = pd.read_csv('house_df6.csv')
    st.markdown("<h1 style='text-align: center; color: #FF851B;'>House Price Predictor</h1><hr>'", unsafe_allow_html=True)
    try:
        if choice == 'EDA':
            st.title("Exploratory Data Analysis")
            st.markdown('<style>h1{color: NAVY;}</style>', unsafe_allow_html=True)
            if house_data is not None:
                if st.checkbox("Show Data:"):
                    st.write(house_data.head())
                if st.checkbox("Show Shape"):
                    st.write(house_data.shape)
                if st.checkbox("Show Datatype"):
                    st.write(house_data.dtypes)
                if st.checkbox("Show Statistical Of The Data"):
                    st.write(house_data.describe())
                    st.markdown("Wow, 16 BHK ")
                if st.checkbox("Show Value Count"):
                    all_columns = house_data.columns
                    selected_column = st.selectbox("Select One Column", all_columns)
                    value_count = house_data[selected_column].value_counts()
                    st.write(value_count)

        elif choice == 'Plot':
            st.title("Explore The Data")
            st.markdown('<style>h1{color: OLIVE;}</style>', unsafe_allow_html=True)
            if st.checkbox("Show Pairwise Relationship"):
                loading_plot = st.text("Loading Plot...")
                sns.pairplot(house_data)
                st.pyplot()
                loading_plot.text("Loading Plot...Done!")

            if st.checkbox("Show Data Distribution"):
                loading_plot = st.text("Loading Plot...")
                i = 0
                for col in house_data.drop(['location'], axis=1):
                    i += 1
                    plt.subplot(2,2,i)
                    sns.distplot(house_data[col], rug=True, rug_kws={'color':'g'},
                                kde_kws={"color": "k", "lw": 3, "label": "KDE"},
                                hist_kws={"histtype": "step", "linewidth": 3,"alpha": 1, "color": "g"}, label=col)
                    plt.gcf().set_size_inches(10,20)
                st.pyplot()
                loading_plot.text("Loading Plot...Done!")

            if st.checkbox("Show Home Price BHK Wise"):
                loading_plot = st.text("Loading Plot...")
                c = alt.Chart(house_data).mark_circle().encode(x='BHK', y='price')
                st.altair_chart(c, use_container_width=True)
                loading_plot.text("Loading Plot...Done!")

            if st.checkbox("Show Bath Vs BHK"):
                loading_plot = st.text("Loading Plot...")
                c = alt.Chart(house_data).mark_circle().encode(x='BHK', y='bath')
                st.altair_chart(c, use_container_width=True)
                loading_plot.text("Loading Plot...Done!")

            if st.checkbox("Show How many house are present area wise[TOP 10]"):
                loading_plot = st.text("Loading Plot...")
                plt.figure(figsize=(12,10))
                sns.barplot(x=house_data['location'].value_counts().head(10).index, y=house_data['location'].value_counts().head(10).values, palette='rainbow')
                plt.xticks(rotation=30)
                st.pyplot()
                loading_plot.text("Loading Plot...Done!")

            if st.checkbox("Show Total price area wise"):
                loading_plot = st.text("Loading Plot...")
                #value = st.sidebar.selectbox("Select", house_data['location'])
                #st.write(value)
                value = house_data[['location','price']].groupby(['location'])['price'].agg('sum').sort_values(ascending=False)
                st.write(value)
                #st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
                loading_plot.text("Loading Plot...Done!")

            if st.checkbox("Show Correlation Heatmap"):
                loading_plot = st.text("Loading Plot...")
                sns.heatmap(house_data.corr(), annot=True)
                st.pyplot()
                loading_plot.text("Loading Plot...Done!")


            if st.checkbox("Show Actual and Predicted Value Graph"):
                loading_plot = st.text("Loading Plot...")
                st.image('download.png', width=900)
                loading_plot.text("Loading Plot...Done!")

        else:
            st.title("Prediction")
            location = st.selectbox("Select Location", house_data7.iloc[:,4:].columns)
            st.markdown('<style>h1{color: TEAL;}</style>', unsafe_allow_html=True)
            sqft = st.slider("What is your square feet of room?", int(house_data7.total_sqft.min()), int(house_data7.total_sqft.max()), int(house_data7.total_sqft.mean()))
            bhk = st.slider("How many bedrooms?", int(house_data7.BHK.min()), int(house_data7.BHK.max()), int(house_data7.BHK.mean()))
            bath = st.slider("How many bathrooms?", int(house_data7.bath.min()), int(house_data7.bath.max()), int(house_data7.bath.mean()))



            if st.button("Predict"):
                result = house_price_prediction(location, sqft, bhk, bath)
                if result <= 0:
                    st.error("There is something wrong with your inputs")
                else:
                    st.success("Prediction: Rs.{:,}".format(result))
    except Exception as e:
        return "Something went wrong"


if __name__ == '__main__':
    menuCategory()

