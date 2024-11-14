import streamlit as st
from datetime import datetime
import pytz

st.set_page_config (
    page_title = "NutriHome",
    page_icon = "🍕",
)

# Define Time
timezone = pytz.timezone("Asia/Bangkok")
now = datetime.now(timezone)

# Initialize session state variables
if "date" not in st.session_state:
    st.session_state.date = ""
if "day_of_week" not in st.session_state:
    st.session_state.day_of_week = ""
if "meal" not in st.session_state:
    st.session_state.meal = ""

# Set date and hour
st.session_state.date = now.strftime("%d-%m-%Y")
hour = int(now.strftime("%H"))

# Set day of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
st.session_state.day_of_week = days[now.weekday()]

# Set meal based on hour
if 0 <= hour < 10:
    st.session_state.meal = "Breakfast"
elif 10 <= hour < 16:
    st.session_state.meal = "Lunch"
else:
    st.session_state.meal = "Dinner"

# Check if user session state exists, if not, initialize it
if "user" not in st.session_state:
    st.session_state.user = {
        "id": 0,
        "fullname": "",
        "username": "",
        "avatar": "",  # Path to user avatar image
        "dob": "",  # Date of birth
        "age": 0,
        "gender": "",  # User's gender
        "height": 0,  # Height in cm
        "weight": 0,  # Weight in kg
        "bmi": 0.0,
        "disease": "",
        "allergen": "",
        "activity_level": "",  # Activity level of the user
        "absorbed_carbs": 0,
        "absorbed_protein": 0,
        "absorbed_fat": 0,
        "absorbed_calories": 0,
        "target_carbs": 0,  # Daily target carbohydrates in grams
        "target_protein": 0,  # Daily target protein in grams
        "target_fat": 0,  # Daily target fat in grams
        "target_calories": 0,  # Daily calorie target
        "family_id": 0,  # Identifier for the family group
    }

#Food details (Show food details)
if "food_details" not in st.session_state:
    st.session_state.food_details = {
        "name" : "",
        "image" : "",
        "rating" : 0.0,
        "cooking_time" : 0,
        "calories" : 0,
        "protein" : 0,
        "carbs" : 0,
        "fat" : 0,
        "steps" : [],
        "ingredients" : []
    }

#Weekly menu (Show weekly menu)
if "weekly_menu" not in st.session_state:
    st.session_state.weekly_menu = {
        "Monday": {
            "Breakfast": {
                "listOfFoods": [],
                "eaten": 0, #Sua thanh 0, 1
            },
            "Lunch": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "Tuesday": {
            "Breakfast": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "Wednesday": {
            "Breakfast": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "Thursday": {
            "Breakfast": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "Friday": {
            "Breakfast": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "Saturday": {
            "Breakfast": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "Sunday": {
            "Breakfast": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [],
                "eaten": 0,
            },
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        }
    }

if "today_nutrients" not in st.session_state:
    st.session_state.today_nutrients = {
        "Carbs": 0,
        "Protein": 0,
        "Fat": 0,
        "Calories": 0
    }

#History
if "history" not in st.session_state:
    st.session_state.history = {
        "Today": {
            "Breakfast": {
                "listOfFoods": [

                ],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [

                ],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [
 
                ],
                "eaten": 0,
            },
            "Date": "",
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "Yesterday": {
            "Breakfast": {
                "listOfFoods": [

                ],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [

                ],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [

                ],
                "eaten": 0,
            },
            "Date": "",
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        },
        "theDayBefore": {
            "Breakfast": {
                "listOfFoods": [

                ],
                "eaten": 0,
            },
            "Lunch": {
                "listOfFoods": [
 
                ],
                "eaten": 0,
            },
            "Dinner": {
                "listOfFoods": [

                ],
                "eaten": 0,
            },
            "Date": "",
            "Carbs": 0,
            "Protein": 0,
            "Fat": 0,
            "Calories": 0
        }
    }

#Searching list
if "searchingList" not in st.session_state:
    st.session_state.searchingList = [
        {
            "id": 0,
            "name": "",
            "image": "",
            "cooking_time": 0,
            "rating": 0
        },
    ]

# Add Member
if "addMember" not in st.session_state:
    st.session_state.addMember = []
if "addMemberUsername" not in st.session_state:
    st.session_state.addMemberUsername = []

# Family
if "family" not in st.session_state:
    st.session_state.family = {
        "id": 0,
        "name": "",
        "avatar": "family_images/nutrihome_avatar.jpg",
        "description": "",
        "member": [
            {
                "user_id": 0,
                "username": "",
                "name": "",
                "profile_image": "",  # Path to user avatar image
                "currentCalo": 0,
                "currentProtein": 0,
                "currentFat": 0,
                "currentCarbs": 0,
                "targetCalo": 0,  # Daily target carbohydrates in grams
                "targetCarbs": 0,  # Daily target protein in grams
                "targetFat": 0,  # Daily target fat in grams
                "targetProtein": 0,  # Daily calorie target
            },
        ]
    }

# Shopping list
if "shoppingList" not in st.session_state:
    st.session_state.shoppingList = []

# Forum
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "post_id": 0,
            "author_id": 0,
            "author": "",
            "author_username": "",
            "title": "",
            "content": "",
            "image": "",
            "created_at": "",
            "react": False,
            "total_reacts": 0,
            "comments": []
        },
    ]
    
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "login_page" not in st.session_state:
    st.session_state.login_page = False

if "language" not in st.session_state:
    st.session_state.language = "Vietnamese"

def logout():
        st.session_state.logged_in = False
        st.session_state.login_page = ""
        st.session_state.register = False

        st.session_state.user = {
            "id": 0,
            "fullname": "",
            "username": "",
            "avatar": "",  # Path to user avatar image
            "dob": datetime(2000, 1, 1).strftime("%d-%m-%Y"),  # Date of birth
            "age": 0,
            "gender": "",  # User's gender
            "height": 0,  # Height in cm
            "weight": 0,  # Weight in kg
            "bmi": 0.0,
            "disease": "",
            "allergen": "",
            "activity_level": "",  # Activity level of the user
            "absorbed_carbs": 0,
            "absorbed_protein": 0,
            "absorbed_fat": 0,
            "absorbed_calories": 0,
            "target_carbs": 0,  # Daily target carbohydrates in grams
            "target_protein": 0,  # Daily target protein in grams
            "target_fat": 0,  # Daily target fat in grams
            "target_calories": 0,  # Daily calorie target
            "family_id": 0,  # Identifier for the family group
        }

        st.session_state.food_details = {
            "id": 0,
            "name" : "",
            "image" : "",
            "rating" : 0.0,
            "cooking_time" : 0,
            "calories" : 0,
            "protein" : 0,
            "carbs" : 0,
            "fat" : 0,
            "step" : "",
            "ingredients" : ""
        }

        st.session_state.weekly_menu = {
            "Monday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "Tuesday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "Wednesday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "Thursday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "Friday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "Saturday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "Sunday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            }
        }

        st.session_state.history = {
            "Today": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Date": "",
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "Yesterday": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Date": "",
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            },
            "theDayBefore": {
                "Breakfast": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Lunch": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Dinner": {
                    "listOfFoods": [
                        { 
                            "id": 0,
                            "name": "",
                            "image": ""
                        },
                    ],
                    "eaten": False,
                },
                "Date": "",
                "Carbs": 0,
                "Protein": 0,
                "Fat": 0,
                "Calories": 0
            }
        }

        st.session_state.searchingList = [
            {
                "id": 0,
                "name": "",
                "image": "",
                "cooking_time": 0,
                "rating": 0
            },
        ]

        st.session_state.addMember = []
        st.session_state.addMemberUsername = []

        st.session_state.family = {
            "id": 0,
            "name": "",
            "avatar": "",
            "description": "",
            "member": [
                # {
                #     "id": 0,
                #     "username": "",
                #     "fullname": "",
                #     "avatar": "",  # Path to user avatar image
                #     "absorbed_carbs": 0,
                #     "absorbed_protein": 0,
                #     "absorbed_fat": 0,
                #     "absorbed_calories": 0,
                #     "target_carbs": 0,  # Daily target carbohydrates in grams
                #     "target_protein": 0,  # Daily target protein in grams
                #     "target_fat": 0,  # Daily target fat in grams
                #     "target_calories": 0,  # Daily calorie target
                # },
            ]
        }

        st.session_state.shoppingList = []

        st.session_state.posts = [
            {
                "post_id": 0,
                "author_id": 0,
                "author": "",
                "author_username": "",
                "title": "",
                "content": "",
                "image": "",
                "created_at": "",
                "react": False,
                "total_reacts": 0,
                "comments": []
            },
        ]
        st.rerun()

login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

home = st.Page("pages/home.py", title="Home", icon=":material/home:")

profile = st.Page("pages/personal/profile.py", title="Profile", icon=":material/account_circle:")
settings = st.Page("pages/personal/settings.py", title="Settings", icon=":material/bug_report:")

weeklyMenu = st.Page("pages/features/weeklyMenu.py", title="Weekly Menu", icon=":material/assignment:")
recipes = st.Page("pages/features/recipes.py", title="Recipes", icon=":material/content_paste_search:")
history = st.Page("pages/features/history.py", title="History", icon=":material/history:")
family_health = st.Page("pages/features/family_health.py", title="Family Health", icon=":material/diversity_1:")
ingredient_safety = st.Page("pages/features/ingredient_safety.py", title="Ingredient Safety", icon=":material/health_and_safety:")
community = st.Page("pages/features/community.py", title="Community", icon=":material/forum:")


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "": [home],
            "Features": [weeklyMenu, recipes, history, family_health, ingredient_safety, community],
            "Personal": [profile, settings, logout_page],
        }
    )
else:
    pg = st.navigation([home])

    if st.session_state.login_page:
        pg = st.navigation([login_page])
    else:
        pg = st.navigation([home])

pg.run()