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
  print(df)


if __name__ == "__main__":
  # run main
    main()
