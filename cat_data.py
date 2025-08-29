def main():
  # pandas 
  import pandas as pd

  # define df
  df = pd.DataFrame([
    ['green', 'M', 10.1, 'class2']
    ,['red', 'L', 13.5, 'class1']
    ,['blue', 'XL', 15.3, 'class2']
  ])

  # label columns of df
  df.columns = ['color', 'size', 'price', 'classlbl']

  # print df
  print("Categorical data encoding with pandas \n")
  print(df)

  # mapping ordinal features dictionary
  size_mapping = {'XL':3
                ,'L':2
                ,'M':1
                }

  # ivnerse mapping dictionary
  inv_size_mapping = {v: k for k, v in size_mapping.items()}
  
  # apply mapping to column 'size'
  df['size'] = df['size'].map(size_mapping)

  # print df
  print("Mapping ordinal features \n")
  print(df)

# print inv
print("Inverse size mapping \n")
print(df['size'].map(inv_size_mapping))

if __name__ == "__main__":
  # run main
    main()
