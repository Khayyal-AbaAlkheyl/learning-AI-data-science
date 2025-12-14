# With that background, let's see an example of how we would do this in pandas, where we would use the merge
# function.
import pandas as pd

# First we create two DataFrames, staff and students.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
# And lets index these staff by name
staff_df = staff_df.set_index('Name')
# Now we'll create a student dataframe
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
# And we'll index this by name too
student_df = student_df.set_index('Name')

# And lets just print out the dataframes
print(staff_df.head())
print()
print(student_df.head())
print()
# There's some overlap in these DataFrames in that James and Sally are both students and staff, but Mike and
# Kelly are not. Importantly, both DataFrames are indexed along the value we want to merge them on, which is
# called Name.
# If we want the union of these, we would call merge() passing in the DataFrame on the left and the DataFrame
# on the right and telling merge that we want it to use an outer join. We want to use the left and right
# indices as the joining columns.

print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))
print()

# We see in the resulting DataFrame that everyone is listed. And since Mike does not have a role, and John
# does not have a school, those cells are listed as missing values.

# If we wanted to get the intersection, that is, just those who are a student AND a staff, we could set the
# how attribute to inner. Again, we set both left and right indices to be true as the joining columns
print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))
print()

# And we see the resulting DataFrame has only James and Sally in it. Now there are two other common use cases
# when merging DataFrames, and both are examples of what we would call set addition. The first is when we
# would want to get a list of all staff regardless of whether they were students or not. But if they were
# students, we would want to get their student details as well. To do this we would use a left join. It is
# important to note the order of dataframes in this function: the first dataframe is the left dataframe and
# the second is the right

print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))
print()
# You could probably guess what comes next. We want a list of all of the students and their roles if they were
# also staff. To do this we would do a right join.
print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))
print()
# We can also do it another way. The merge method has a couple of other interesting parameters. First, you
# don't need to use indices to join on, you can use columns as well. Here's an example. Here we have a
# parameter called "on", and we can assign a column that both dataframe has as the joining column

# First, lets remove our index from both of our dataframes
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

# Now lets merge using the on parameter
print(pd.merge(staff_df, student_df, how='right', on='Name'))


"""
This code demonstrates how to combine datasets in pandas using the `merge()` function. 
It shows different join types, how indexes affect merging, and how to merge on columns 
when needed.

Key concepts:

- Preparing DataFrames:
  - Two DataFrames (`staff_df` and `student_df`) are created and indexed by the `Name` column. 
    This index becomes the key used for merging.

- Merging with Different Join Types:
  - **Outer Join** (`how='outer'`): Produces the union of both DataFrames. 
    Everyone appears in the result; unmatched fields become missing values.
      pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)

  - **Inner Join** (`how='inner'`): Produces the intersection. 
    Only names present in *both* DataFrames are included.

  - **Left Join** (`how='left'`): Returns all rows from the left DataFrame (`staff_df`). 
    If a staff member is also a student, the student info is included.

  - **Right Join** (`how='right'`): Returns all rows from the right DataFrame (`student_df`). 
    Student details appear whether or not they are staff.

- Joining on Columns Instead of Index:
  - Resetting the index with `reset_index()` converts the index back to a normal column.
  - After that, merges can be done using the `on` parameter:
      pd.merge(staff_df, student_df, how='right', on='Name')

This pattern is foundational in data wrangling: merging tables by shared identifiers, 
choosing the appropriate join type, and deciding whether indexes or columns should 
serve as the merge keys.
"""