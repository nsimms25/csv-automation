import pandas as pd

raw_df = pd.read_csv('example_tasks.csv', index_col=0)

#print(raw_df)

case_list = raw_df.case_number.unique()
#print(case_list)
#print(len(case_list))

no_dup_cases = raw_df.drop_duplicates(["case_number"])
#print(no_dup_cases)

occur = no_dup_cases.groupby('performer').size()
#print(occur)
#print(occur['Andrew'])
#print(occur['Nick'])
#print(occur['Jane'])

#### Parse Title Possible Examples ####

# Potential Options 
title1 = '20230626-CASE_NUMBER-SITE-NS-AUGMENT-16' # Append Type and count at end (probably easiest).

case_type = title1.split('-')[-2]
case_count = int(title1.split('-')[-1])

case_type_count = (case_type, case_count)

print(case_type_count)
