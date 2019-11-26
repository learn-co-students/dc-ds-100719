
# Module 4 -  Final Project Specifications

## Introduction

In this document, we'll review all the guidelines and specifications for the final project for Module 4.

## Objectives

* Identify all required aspects of the Final Project for Module 4
* Describe all required deliverables
* Summarize what constitutes a successful project

### Final Project Summary

Another module down--you're absolutely crushing it! For this project, you'll get to flex your **Regression & Classification** muscles!

For this module's final project, we're going to put your new found **Regression & Classification** skills to the test.

### The Project

For this project, you will be acting as a consultant for a fictional firm. As a part of your data exploration, come up with a _driving question_ based on this data. <br>

![crispdm](https://www.stellarconsulting.co.nz/wp-content/uploads/2017/08/CRISP-DM_Process_1000x600.jpg)

For example, if you were given a data set of housing price data for a given city, a driving question might be:

> Based on forecasts, what are the top 5 best zip codes for us to invest in?


## The Deliverables

The goal of this project is to have you complete a very common real-world task in regard to Regression & Classification Modeling. However, real world problems often come with a significant degree of ambiguity, which requires you to use your knowledge of statistics and data science to think critically about and answer.

In short, to pass this project, demonstrating the quality and thoughtfulness of your **overall recommendation** is at least as important as successfully building your models!

In order to successfully complete this project, you must have:

* A well-documented master **_Jupyter Notebook_** explaining the rational and decisions of your project.
* A dataset that is **not overly used** online in data science examples. 
* Well organized code in modularized .py files.
* Should be able to justify your decisions in your notebook. Some decisions may include: Was there data leakage? Which algorithms did you use and why? Any tuning of the model? How did you set a certain parameter to a certain value? Cross-validation, normalization, etc.
* A **_Presentation_** that explains your rationale and methodology.




### Master Jupyter Notebook Must-Haves

1. You must source & clean your data.  **All boring stuff should be pushed to a .py file** that is imported.  A single data set (albeit possibly from multiple sources) should be able to support all of the following requirements.
2. You can do a regression or a classification, **compare different models and compare their performances**. Be sure that you include justifications of these decisions in your technical notebook.
3. Visualizations to support each of your models built. *Make sure to check for any assumptions.

#### Organization/Code Cleanliness

The notebook should be well organized, easy to follow, and code is modularized and commented where appropriate.

* High level: 
 - The notebook contains well-formatted, professional looking markdown cells.
 - Functions are organized well in different name-space related `.py` files (data cleaning, feature engineering, modeling, assumption checking, etc) 
 - All functions have docstrings that act as professional-quality documentation
 - All `.py` files should use PEP8 style guide
* The notebook is written to _technical audiences_ with a way to both understand your approach and reproduce your results. The target audience for this deliverable is other data scientists looking to validate your findings.
* Data visualizations you create should be clearly labeled and contextualized--that is, they fit with the surrounding code or problems you're trying to solve. No dropping data visualizations randomly around your notebook without any context!

### Github Guidelines
- Project deliverables should be stored in a GitHub repo with a descriptive name (`Predicting Impact of USAID grants on Women's Safety in Congo` vs `Mod 4 project`)
- Repo must be well formatted and organized and contains:
 - LICENSE
 - README.md that included a link to the slide-deck, structure of the repo, partner
 - Data Folder with clearly marked final dataset
 - A Notebook Folder containing all older versions or partial versions of your notebooks
 - Utils folder with all your .py files
 - Master notebook in the main repo (outside of the notebook folder)
- Final project material should live on the *master* branch
- Individuals over the course of the project, should work on their own branch, daily merges to master branch. 

### Visualizations

##### EDA Visualizations  
Exploratory data analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods.  This is a key element of all data science projects.  It is important to conduct EDA before doing any modeling so that you understand the characteristics of your data, to help with data cleaning, and to apply appropriate models.

The objectives of EDA are to:

- To find key business insights that modeling is not necessary for
- To uncover anomalies in your data to assist in data cleaning
- Suggest hypotheses about the causes of observed phenomena
- Assess assumptions of any model you are going to use
- Support the selection of appropriate models and techniques


##### Model/Metric Visualizations

Regression & Classification are areas of data science that lend themselves well to intuitive data visualizations. **_Any findings worth mentioning in this problem are probably also worth visualizing_**. Your notebook should make use of data visualizations as appropriate to make your findings obvious to any readers.

Also, remember that if a visualization is worth creating, then it's also worth taking the extra few minutes to make sure that it is easily understandable and well-formatted. When creating visualizations, make sure that they have:

* A title
* Clearly labeled X and Y axes, with appropriate scale for each
* A legend, when necessary
* No overlapping text that makes it hard to read
* An intelligent use of color--multiple lines should have different colors and/or symbols to make them easily differentiable to the eye (**please, no rainbow color scheme**), color should be used to represent something!
* An appropriate amount of information--avoid creating graphs that are "too busy"--for instance, don't create a line graph with 25 different lines on it

<center><img src='http://genywealth.com/wp-content/uploads/2010/03/line-graph.php_.png' height=100% width=100%>
There's just too much going on in this graph for it to be readable--don't make the same mistake! (<a href='http://genywealth.com/wp-content/uploads/2010/03/line-graph.php_.png'>Source</a>)</center>

### Presentation Must-Haves

Your Non-technical presentation should:

- Be aimed at a non-technical audience
 - Avoid technical jargon and explain results in a clear, actionable way for non-technical audiences.
- Contain between 5-10 professional quality slides including:
 - The components of the slide-deck template located [HERE](https://docs.google.com/presentation/d/1e6-8R05wFGk7qsCsi6zOwweMNze1y4phY0_ERdbRVM4/edit?usp=sharing)
 - A high-level overview of your methodology and findings including the 5 zip codes you recommend investing in (for example)
 - A brief explanation of what metrics you defined as "best" in order complete this project
- Take no more than 5 minutes to present

### Technical Interview

After your non-technical presentation you will have 15 minutes to show your technical work including:

- README.md file
- Commit History
- Technical Notebook
- .py files
- Doc strings for functions
- Explain rationale for technical decision
- Explain final model in technical language


### Groups:

1: Allison & Seoho

2: Irving & Steven

3: Anil & Brad

4: Buddy

5: Nicole


### Timeline:
- Wednesday 11/27 Project Kick-Off
- Monday 12/2 - project pitch to coaches
 - dataset should be finalized and explored
 - Should have baseline model by EOD
- Tuesday 12/3 check in and feedback from instructor 
- Wednesday 12/4 Project presentations, technical interview, and Science Fair