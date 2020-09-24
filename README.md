# home-price-prediction

### **Demo** 
<hr/>

Link:https://home-price-prediction.herokuapp.com/

![Screenshot (72)](https://user-images.githubusercontent.com/51736427/85556717-bd689300-b644-11ea-9011-98f76d1fefbe.png)

![Screenshot (72)](https://user-images.githubusercontent.com/51736427/85558085-0a993480-b646-11ea-956f-2d011ab2cebb.png)

![Untitled](https://user-images.githubusercontent.com/51736427/85558615-872c1300-b646-11ea-9dc5-fdff67a96ae9.png)

### **Overview**
<hr/>

This is the **Streamlit** base **Machine learning** web app to predict the house price in Bangalore by taking different parameter as an input like Location, Square Feet, Bedrooms and Bathrooms  and  deploy  a  model  on the  Heroku platform.

The project contain three components:

  1. EDA: EDA stands for **Exploratory Data Analysis**. It show **DataFrame**, **Shape of the data**, **Datatype of each columns** Etc.
  2. Plot: This part show the essential plot of house dataset. Like **Correlation of each variable**, **Show how data is distributed** and many more.
  3. Prediction: The model takes an **Location**, **Square Feet**, **Bedrooms**, **Bathrooms** as an input and predict the **price**.


### **Technical Aspect**
<hr />

1. Building and hosting a Streamlit web app on Heroku.<br/>
      
      - Used **Numpy** and **Pandas** to manipulate data.
      
      - Used **Matplotlib** and **Seaborn** to explore the data with different plot. I also used streamlit buil-in chart functionality to plotting the plot.
      
      - I used **Multi Linear Regression** to predict the price.
      
### **Installation**
<hr />

The Code is written in Python 3.7. If you don't have Python installed you can find it <a href="https://www.python.org/downloads/">here</a>. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after <a href="https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository">cloning</a> the repository:
    
   - Additional packages that are required are: Numpy, Pandas, Matplotlib, Seaborn, scikit-learn.
   
   - Download all packages from <a href="https://pypi.org/">here.</a>
   
   - For streamlit you can just hit below command in cmd.
    
          pip install streamlit
          
     
  

### **Deployement on Heroku**

  To deploy streamlit web app, There are some file we need to add like setup.sh, requirements.txt in our repository.

  1. Click on this <a href="https://dashboard.heroku.com/">Link</a>
  2. Create a new account by click on sign up button.
  3. Login with Email and Password.
  4. After login, screen redirect to the Dashboard. Click on upper top right corner to create a new app.
  5. Give proper name of your app and choose united states america.
  6. Heroku create a empty app setup for you. Next step is to go on **Deploy** menu.You can see that Heroku provide different-different method to deploy the web-app.
     We deploy by using **Github** repository. For that, click on github icon and they ask for a username and password of your github account. After that heroku connect with          your github account.
  7. In same page, go to the App connected to Github section and search repository which is hold all your essential file(Make sure that you have to create repository first then     only heroku can able to search that repository).
  8. Next step is to click on the connect button and Heroku able to connect with your repository.
  9. In same page, go to the Manual Deploy section and click on **Deploy Branch**. Before clicking onto that button makesure that you need to add all neccessary file in your        repository.
  9. Heroku installed all packages. BOOM! After sometime heroku able to deploy your app and it will give you link for your app.
  

### **Technologies Used** ###

![1_3CXBOKNql4qS-lRyHT3pqw](https://user-images.githubusercontent.com/51736427/85572764-e6902000-b652-11ea-8826-91786e303f6b.png)
![mjnw24k71dpqmcqg6mno](https://user-images.githubusercontent.com/51736427/85573065-2e16ac00-b653-11ea-8fa5-c5e599ebdfcf.png)
![images](https://user-images.githubusercontent.com/51736427/85573181-4b4b7a80-b653-11ea-8791-90c346f0f12c.png)

   
