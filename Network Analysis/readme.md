# Data Science for VCs

Why is Data Science important for VCs?

I = T - (R + P + M)

where:

- I is the total time allotted to making new investments in startups
- T is the total time needed to manage the fund administratively and raise new capital
- P is the time needed to work with and support the fund's portfolio
- M is the miscellaneous time used for networking events, public events, etc to raise firm's brand

![Image for post](https://miro.medium.com/max/529/1*gwemYooSraE3sN99ACf3DA.png)

### Decision Analysis

- 100/4000 of the top investments making 100% of the profits
- There is a lot of uncertainty in VC
- Decision Analysis can help with tackling uncertainty in VC

#### Decision Making Process

- Sort Qualitatively (Market, Team, Fit)
- Create Market Map (Unit Sales, Price, Customer Segment)
- Assess Risks (Market, Product, Team, Financial)
- Quantify Uncertainties (High, Base, Low)
- Perform Sensitivity Analysis 

  ![Figure 6. Sensitivity Analysis Showing Inkling's Top Uncertainties.](http://kauffmanfellows.org/wp-content/uploads/vol3_Korver_Figure6.jpg)

- Calculate Risk / Return (Early Stage Success, Cross Chasm)

![Figure 4. Evaluation of Inkling's Lifestage Risks.](http://kauffmanfellows.org/wp-content/uploads/vol3_Korver_Figure4.jpg)

### Data Collection

- Collect data on LPs, other VC firms, and angel investors
- Data from portfolio companies (Business and Financial Metrics)
- Data from startups from websites such as CrunchBase
- Market reports and public data
- Searches and keywords usages on specific problems
- Social and professional content on startups and reviews
- Customer engagement metrics
- Hiring activities and employee / founder key backgrounds

All this data needs to be warehoused.

### Due Diligence

Some VCs send a data analyst to the startup office to collect raw data to conduct their own analysis on startups.

### Market Trends

Other VCs use supervised and unsupervised learning models to predict market trends, or to create clusters of startups as well as other funds. 

### Sourcing and Scoring Algorithms

Instead of giving binary 0 to 1 possible scores, calculating using probabilities is more accurate. Many VC firms now have sourcing or scouting algorithms. Algorithms crawl websites to find company profiles to notify analysts. Otherwise, other algorithms use metrics to score startups.

### Others

Other uses of data include to support their portfolio startups or for fundraising

### Network Charts

One way of sourcing for deal-flow is through visualizing connections among VC funds based on their co-investments.

A good way of doing so is through network charts.

![Image source: NetworkX: Network Analysis with Python, Petko Georgiev -Computer Laboratory, University of Cambridge](https://miro.medium.com/max/1322/1*wHNJVGV6MiPYr3OZdSYHUw.png)

#### Why Network Charts?

Network charts are useful to VC funds that intend to understand:

- Competitors' interactions
- Monitoring 

Refer to Network Analysis notebook to get a sample Network Analysis Script

### Case Study: Hone Capital

Hone Capital created a machine learning model from more than 30,000 deals from Crunchbase, PitchBook, etc

They looked at whether a team made it to a series A round, and analyzed 400 data points for each deal. They identified 20 characteristics for seed deals as most predictive of future success.

Interesting Insights:

- Failed to advanced had an average seed investment of 0.5M and below
- Average that did go to series A had around 1.5M
- Once, a deal that seemed bad by human intuition had a 80% chance of success, and after more conversation they realised the model was quite accurate
- Key KPI: Whether a portfolio company goes on to raise a follow-on rounding

### Other Case Studies:

- 645 Ventures: Using data to calculate metrics for deal sourcing; automation work
- Ardian: Partners with startups to collect and analyze unstructured market data
- Connectic Ventures: Analyzes and ranks startups
etc...

There are also startups in this space:

- Kogneitcs: Identify interesting deals based on frameworks
- Valsys: Provides professionals with tools to make data driven decisions


### References

https://towardsdatascience.com/data-science-in-venture-capital-8c13ec0c8458
https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/a-machine-learning-approach-to-venture-capital#
https://vcpreneur.com/how-vcs-lps-apply-data-science-to-make-informed-investment-decisions-527c917a3edf

