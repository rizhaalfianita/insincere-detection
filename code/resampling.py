import pandas as pd

def resampling_data(raw_df):
    sincere_df = raw_df[raw_df.target == 0]
    insincere_df = raw_df[raw_df.target == 1]

    resample_size = 2000
    if len(sincere_df) > resample_size:
        sincere_df = sincere_df.sample(resample_size)
    
    if len(insincere_df) > resample_size:
        insincere_df = insincere_df.sample(resample_size)

    fix_df = pd.concat([sincere_df, insincere_df], ignore_index=True)
    return fix_df