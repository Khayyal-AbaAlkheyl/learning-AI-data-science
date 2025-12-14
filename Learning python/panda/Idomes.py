# Let's start by bringing in our data processing libraries
import pandas as pd
import numpy as np
# And we'll bring in some timing functionality too, from the timeit module
import timeit
from pathlib import Path
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# And let's look at some census data from the US (use script-relative path)
csv_path = Path(__file__).resolve().parent / 'census.csv'
if not csv_path.exists():
  raise FileNotFoundError(f"Could not find 'census.csv' at: {csv_path}\n"
              "Put the file in the same folder as this script or update the path.")
df = pd.read_csv(csv_path)
print(df.head())
print()
print()

# The first of the pandas idioms I would like to talk about is called method chaining. The general idea behind
# method chaining is that every method on an object returns a reference to that object. The beauty of this is
# that you can condense many different operations on a DataFrame, for instance, into one line or at least one
# statement of code.

# Here's the pandorable way to write code with method chaining. In this code I'm going to pull out the state
# and city names as a multiple index, and I'm going to do so only for data which has a summary level of 50,
# which in this dataset is county-level data. I'll rename a column too, just to make it a bit more readable.
print((df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})).head())
print()
print()


# Lets walk through this. First, we use the where() function on the dataframe and pass in a boolean mask which
# is only true for those rows where the SUMLEV is equal to 50. This indicates in our source data that the data
# is summarized at the county level. With the result of the where() function evaluated, we drop missing
# values. Remember that .where() doesn't drop missing values by default. Then we set an index on the result of
# that. In this case I've set it to the state name followed by the county name. Finally. I rename a column to
# make it more readable. Note that instead of writing this all on one line, as I could have done, I began the
# statement with a parenthesis, which tells python I'm going to span the statement over multiple lines for
# readability.

# Here's a more traditional, non-pandorable way, of writing this. There's nothing wrong with this code in the
# functional sense, you might even be able to understand it better as a new person to the language. It's just
# not as pandorable as the first example.

# First create a new dataframe from the original
df = df[df['SUMLEV']==50] # I'll use the overloaded indexing operator [] which drops nans
# Update the dataframe to have a new index, we use inplace=True to do this in place
df.set_index(['STNAME','CTYNAME'], inplace=True)
# Set the column names
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
print(df.head())
print()
print()

# As you can see, the second approach is much faster! So, this is a particular example of a classic time
# readability trade off.

# You'll see lots of examples on stack overflow and in documentation of people using method chaining in their
# pandas. And so, I think being able to read and understand the syntax is really worth your time. But keep in
# mind that following what appears to be stylistic idioms might have performance issues that you need to
# consider as well.


"""
This code demonstrates a core pandas idiom called *method chaining*, compares it with a 
more traditional step-by-step approach, and highlights the trade-offs between readability 
and performance.

Dataset:
- Reads U.S. census data from `census.csv`.

Method Chaining (the “pandorable” style):
- A sequence of DataFrame operations is performed in one continuous expression:
    df.where(df['SUMLEV'] == 50)      → keeps only county-level rows; others become NaN  
    .dropna()                         → removes the NaN rows produced by where()  
    .set_index(['STNAME','CTYNAME'])  → creates a multi-index: state → county  
    .rename({...})                    → renames a column for clarity  
- Each method returns a modified DataFrame, allowing the next method to attach directly.
- The resulting chain is compact and expressive, reflecting intent rather than mechanics.

Traditional Step-by-Step Approach:
- Filtering with df[df['SUMLEV'] == 50] directly drops non-matching rows.  
- `set_index(..., inplace=True)` modifies the DataFrame in place.  
- `rename()` is called separately.  
- This style is often easier for beginners to follow but loses the fluency of the chained style.

Performance Note:
- In this example, the step-by-step approach runs significantly faster.  
  Chaining improves readability and reduces boilerplate, but it may introduce 
  intermediate objects that slow execution.

Conceptual Takeaways:
- Method chaining leverages pandas’ design: each method returns a DataFrame.  
- It encourages a clean, linear transformation pipeline.  
- Developers should balance readability with execution time, especially for large datasets.  
- Understanding chained expressions is essential when reading real-world pandas code 
  found in documentation, tutorials, and community solutions.
"""