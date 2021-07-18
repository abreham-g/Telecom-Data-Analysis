# Tellcom-Data-Analysis
# User Overview analysis
For the actual telecom dataset, we are expected to conduct a full User Overview analysis &
the following sub-tasks are your guidance:

    - we Start by identifying the top 10 handsets used by the customers.
    - Then, identifying the top 3 handset manufacturers
    - Next,we identify the top 5 handsets per top 3 handset manufacturer
    - we Make a short interpretation and recommendation to marketing teams
● Next we have to Aggregate per user the following information in the column

    -number of xDR sessions
    -Session duration
    - the total download (DL) and upload (UL) data
    -the total data volume (in Bytes) during this session for each application
    
# User Engagement

● In the current dataset we are expected to track the user’s engagement using the following
engagement metrics:

     -sessions frequency
     -the duration of the session
      -the sessions total traffic (download and upload (bytes))

● Based on the above submit python script and slide :
        -we Aggregate the above metrics per customer id (MSISDN) and report the top 10
         customers per engagement metric
        -Normalize each engagement metric and run a k-means (k=3) to classify customers in
        three groups of engagement.
        -Compute the minimum, maximum, average & total non- normalized metrics for each
        cluster. Interpret your results visually with accompanying text explaining your
        findings.
        -Aggregate user total traffic per application and derive the top 10 most engaged users
         per application
        -Plot the top 3 most used applications using appropriate charts.
        -Using k-means clustering algorithm, group users in k engagement clusters based on
         the engagement metrics:
                        -What is the optimized value of k (use elbow method for this)?
                        -Interpret your findings.



