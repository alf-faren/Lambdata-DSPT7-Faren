def datetime_to_cols(df, col_to_convert):

    col_name_lst = list(df.columns)
    i = col_name_lst.index(col_to_convert)

    df[df[col_name_lst[i]]+'year'] = df[col_to_convert].dt.year
    df[df[col_name_lst[i]]+'month'] = df[col_to_convert].dt.month
    df[df[col_name_lst[i]]+'day'] = df[col_to_convert].dt.day

    df[df[col_name_lst[i]]+'hour'] = df[col_to_convert].dt.hour
    df[df[col_name_lst[i]]+'minute'] = df[col_to_convert].dt.minute
    df[df[col_name_lst[i]]+'second'] = df[col_to_convert].dt.second
    return df
