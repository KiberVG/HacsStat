import pandas as pd
import scipy.stats as stats
#
# # Change to the file you would like to use
df = pd.read_csv("Files/temperaturesbypopulation.csv")
df2 = pd.read_csv("Files/July _Temperatures.csv")
#

#
# # ANOVA Test in Python
# fvalue, pvalue = stats.f_oneway(df['Beltsville'], df['New York'], df['Philadelphia'])
# #print(fvalue, pvalue)
#
# # Now doing the independent T-Tests
#
# # Now doing the T-Tests for all of the individual pairs
#
# ttestbeltsnew = stats.ttest_ind(a=df['Beltsville'], b=df['New York'], equal_var=True)
# print(f"Beltsville and New York: {ttestbeltsnew.pvalue}")
# beltsphili = stats.ttest_ind(a=df['Beltsville'], b=df['Philadelphia'], equal_var=True)
# print(f"Beltsville and Philadelphia: {beltsphili.pvalue}")
# newphili = stats.ttest_ind(a=df['New York'], b=df['Philadelphia'], equal_var=True)
# print(f"New York and Philadelphia: {newphili.pvalue}")

# Now repeating steps A and B with the Kruskal-Wallis test
# allgroups = stats.kruskal(df['Beltsville'], df['New York'], df['Philadelphia'])
# julygroups = stats.kruskal(df2['Beltsville'], df2['New York'], df2['Philadelphia'])
#
# print(f"The p-value for all groups all year-round is {allgroups.pvalue}")
# print(f"The p-value for all groups in july is {julygroups.pvalue}")

# Mann-Whitney tests on the July Populations
# df2 is the Pandas dataframe containing the data for these populations

beltsnew = stats.mannwhitneyu(df2['Beltsville'], df2['New York'])
print(f"Beltsville and New York: {beltsnew.pvalue}")
beltsphili = stats.mannwhitneyu(df2['Beltsville'], df2['Philadelphia'])
print(f"Beltsville and Philadelphia: {beltsphili.pvalue}")
newphili = stats.mannwhitneyu(df2['New York'], df2['Philadelphia'])
print(f"New York and Philadelphia: {newphili.pvalue}")
