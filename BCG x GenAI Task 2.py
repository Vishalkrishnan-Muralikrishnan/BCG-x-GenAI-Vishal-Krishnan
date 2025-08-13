#!/usr/bin/env python
# coding: utf-8

# In[15]:


user_query=input("Enter your Query: ")

def simple_chatbot(user_query):
   if user_query == "What is the total revenue for Microsoft in all 3 years?":
       return "The total revenue is 738,761 Million Dollars."
   elif user_query == "How has net income changed over the years 2023-24 for Microsoft?":
       return "The net income has increased by 15,775 Million Dollars over the last year."
   elif user_query == "How has net income changed over the years 2023-24  for Apple?":
       return "The net income has decreased by 3,259 Million Dollars over the last year."
   elif user_query == "How has net income changed over the years 2023-24 for Tesla?":
       return "The net income has decreased by 7821 Million Dollars over the last year."
   elif user_query == "What is the total revenue for Apple in all 3 years?":
       return "The total revenue is 1,168,648 Million Dollars."
   elif user_query == "What is the total revenue for Tesla in all 3 years?":
       return "The total revenue is 275,925 Million Dollars."
   elif user_query == "How has net income changed over the year 2024-25 for Microsoft?":
       return "The net income has increased by 13,696 Million Dollars over the last year."
   elif user_query == "How has net income changed over the year 2022-23 for Apple?":
       return "The net income has decreased by 2,808 Million Dollars over the last year."
   elif user_query == "How has net income changed over the year 2022-23 for Tesla?":
       return "The net income has increased by 2,387 Million Dollars over the last year."
   elif user_query == "What is the Total Assets Acquired by Microsoft in the 3 years?":
       return "The total Assets Acquired is 1,131,166 Million Dollars."
   elif user_query == "What is the Total Assets Acquired by Apple in the 3 years?":
       return "The total Assets Acquired is 717,563 Million Dollars."
   elif user_query == "What is the Total Assets Acquired by Tesla in the 3 years?":
       return "The total Assets Acquired is 228,688 Million Dollars."
   elif user_query == "What is the Total Liabilities cost for Microsoft in the 3 years?":
       return "The total Liabilities cost is 519,210 Million Dollars."
   elif user_query == "What is the Total Liabilities cost for Apple in the 3 years?":
       return "The total Liabilities cost is 598,467 Million Dollars."
   elif user_query == "What is the Total Liabilities cost for Tesla in the 3 years?":
       return "The total Liabilities cost is 91,399 Million Dollars."
   elif user_query == "What is the Total Operating Activities cost for Microsoft in the 3 years?":
       return "Total Operating Activities cost is 342,292 Million Dollars."
   elif user_query == "What is the Total Operating Activities for Apple in the 3 years?":
       return "Total Operating Activities cost is 350,948 Million Dollars."
   elif user_query == "What is the Total Operating Activities for Tesla in the 3 years?":
       return "Total Operating Activities cost is 42,903 Million Dollars."
   elif user_query == "Hello":
       return "Hi!."
   else:
       return "Sorry, I can only provide information on predefined queries."

simple_chatbot(user_query)


# Summary:
# 
# The Chatbot above is a Rule-Based Chatbot, wherein the Queries taken from user through the INPUT Function will provide an appropriate answer. The Function simple_chatbot(user_query) with argument as User_query is called at the end of the Code to provide appropriate output. Once the Function is called the Python code will check through the simple_chatbot function for the appropriate answer and returns it. If the question is not present then the chatbot replies with sorry message which is in the else functionality. 
# 
# Queries it can Respond to:
# 
# The Chatbot Can respond to basic questions including The Total Liabilities, Total Assets, Total Operating Activities Costs, total revenue and the Net Increase/decrease in total Income for all 3 Companies in all 3 years. For the Change in Net Income, the year must be specified to get appropriate output for net change within that year.
# 
# Limitations:
# 
# The Limitations are Large, 
# 1. It can't answer to any kind of Human based language, despite the query asked by human conveying the same meaning as one of the questions above.
# 2. Any questions asked outside from these pre-defined one's it can't answer.
# 3. Any wrong Caps-lock letter or vice-versa will be identified by the chatbot as a new query, despite asking the query with exact same wordings.
